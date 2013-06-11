class GaussSeidel:

    @staticmethod
    def execute(A, b, x_k, max_depth=10, error=0.000001):
        '''
        Calcula a solucao do sistema Ax = b utilizando o metodo de gauss-seidel
        @param Matrix
        @param Vector
        @param Vector
        @param int (optional)
        @param float (optional)
        @return Vector
        '''
        x_k1 = x_k.copy()
        
        while max_depth > 0 :            
            for i in xrange(A.rows()):
                sum1 = 0
                for j in xrange(0, i):
                    sum1 += A.get(i, j) * x_k1.get(j)
                
                sum2 = 0
                for j in xrange(i+1, A.columns()):
                    sum2 += A.get(i, j) * x_k.get(j)
                    
                x_k1.set(i, (b.get(i) - sum1 - sum2) / A.get(i, i))
            
            if (x_k1 - x_k).norm() / x_k1.norm() < error:
                break
            
            x_k = x_k1.copy()
            
            max_depth -= 1
            
        return x_k1