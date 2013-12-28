from AHPTool.models import Dimension
from AHPTool.models import Rating
import hashlib

class ResultGen:
    def getResult(self):
        dimensions = Dimension.objects.all()
        result_set = []
        set =list( Rating.objects.values('sessionkey').distinct())
        for key in xrange(len(set)):
            #init matrix
            matrix = [[0 for i in xrange(len(dimensions))] for j in xrange(len(dimensions))]
            for i in xrange(len(dimensions)):
                matrix[i][i] = 1
            #fill matrix
            i = k = 0
            while (len(dimensions)>i):
                    for val in dimensions[i:]:
                        if (dimensions[i]!= val):
                            try:
                                r = Rating.objects.get(Dim1 = dimensions[i], Dim2 = val, sessionkey = set[key]['sessionkey'])
                                matrix[i][k] = r.rating
                                matrix[k][i] = 1.0/r.rating
                            except Rating.DoesNotExist:
                                r = Rating.objects.get(Dim1 = val, Dim2 = dimensions[i], sessionkey = set[key]['sessionkey'] )
                                matrix[k][i] = r.rating
                                matrix[i][k] = 1.0/r.rating
                        k+=1
                    i+=1
                    k = i
            print matrix
            #Spaltensummen berechnen 
            summe = 0 
            sumlist = []
            for i in xrange(len(dimensions)):
                for u in xrange(len(dimensions)): 
                    summe += matrix[u][i]
                sumlist.append(summe) 
                summe = 0
            #matrix normen
            for i in xrange(len(dimensions)):
                for u in xrange(len(dimensions)):
                    matrix[u][i] /= (sumlist[i]*1.0)
            #reihensumme berechnen  
        
            sumlist = []
            summe = 0
            for i in xrange(len(dimensions)):
                for u in xrange(len(dimensions)):
                    summe += matrix[i][u]
                sumlist.append(summe)
                summe = 0
            for i in xrange(len(sumlist)):
                sumlist[i] /= len(dimensions)
            for i in xrange(len(sumlist)):
                print sumlist[i]
            result_set.append(sumlist)
        final_vector = [0 for i in xrange(len(dimensions))]
        for i in xrange(len(result_set)):
                for u in xrange(len(result_set[i])):
                    final_vector[u] += ((result_set[i][u]*1.0)/len(result_set))
        #render result to front
        summe = 0
        for i in final_vector:
            summe += i
        
        return (final_vector, summe)