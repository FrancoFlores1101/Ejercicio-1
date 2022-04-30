class clase:
    __id=''
    __dom=''
    __tipo=''
    __contrasenia=''
    def __init__(self,id,dom,tipo,contrasenia):
        self.id=id
        self.dom=dom
        self.tipo=tipo
        self.contrasenia=contrasenia
    def retornaEmail(self):
        return("{}@{}.{}".format(self.id,self.dom,self.tipo))
    def GetDominio(self):
        return(self.dom)
    def CrearCuenta(self,cuenta):
        x=cuenta.split('@')
        self.id=x[0]
        y=x[1].split('.')
        self.dom=y[0]
        self.tipo=y[1]
        self.contrasenia="123"
