class manejador:
    __lista=[]
    def __init__(self):
        self.lista=[]
    def agregarmail(self,unmail):
        self.lista.append(unmail)
    def buscarmail(self,id):
        i=0
        for j in range(len(self.lista)):
            if self.lista[j].id == id:
                i+=1
        if i==0:
            print('no se encontró el mail')
        elif i==1 :
            print ('el mail no se encuentra repetido')
        elif i >= 2 :
            print ('el mail se encuentra repetido')
