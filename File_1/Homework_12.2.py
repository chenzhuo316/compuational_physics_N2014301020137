class SOR(jacobi):
    def evolution(self):
        delta = 10
        self.N = 0
        delta_record = []
        alpha = 2/(1+np.pi/len(self.lattice_in))
        while (delta > 0.00001*len(self.lattice_in)*len(self.lattice_in[0])):
            delta = 0
            for i in range(1,len(self.lattice_in) - 1):
                for j in range(1,len(self.lattice_in[i]) - 1):
                    if (self.lattice_in[i][j] != 1 and self.lattice_in[i][j] != -1):
                        self.lattice_out[i][j] = 0.25*(self.lattice_in[i - 1][j] + self.lattice_in[i + 1][j] + self.lattice_in[i][j - 1] + self.lattice_in[i][j + 1])
                        delta+= abs(self.lattice_out[i][j] - self.lattice_in[i][j])
                        self.lattice_in[i][j] = alpha * (self.lattice_out[i][j] - self.lattice_in[i][j]) + self.lattice_in[i][j]
            #print (self.lattice_out)
            delta_record.append(delta)
            self.N+= 1
        plt.plot(delta_record, label ='SOR algorithm')
        print (self.N)
        print (len(self.lattice_in))
        #print (self.lattice_in)
        return 0    
class SOR_2(jacobi):
    def evolution(self,alpha):
        delta = 10
        self.N = 0
        delta_record = []
        #alpha = 2/(1+np.pi/len(self.lattice_in))
        while (delta > 0.00001*len(self.lattice_in)*len(self.lattice_in[0])):
            delta = 0
            for i in range(1,len(self.lattice_in) - 1):
                for j in range(1,len(self.lattice_in[i]) - 1):
                    if (self.lattice_in[i][j] != 1 and self.lattice_in[i][j] != -1):
                        self.lattice_out[i][j] = 0.25*(self.lattice_in[i - 1][j] + self.lattice_in[i + 1][j] + self.lattice_in[i][j - 1] + self.lattice_in[i][j + 1])
                        delta+= abs(self.lattice_out[i][j] - self.lattice_in[i][j])
                        self.lattice_in[i][j] = alpha * (self.lattice_out[i][j] - self.lattice_in[i][j]) + self.lattice_in[i][j]
            #print (self.lattice_out)
            delta_record.append(delta)
            self.N+= 1
        #plt.plot(delta_record, label ='SOR algorithm')
        print (self.N)
        #print (len(self.lattice_in))
        #print (self.lattice_in)
        return 0  
