class Crear_archivo:
    def __init__(self) -> None:
        self._metodo = 'w'
    
    def archivo(self):

        with open ('primero.txt', self._metodo) as f:
            for i in range(0, 100+1):
                if(i == 100):
                    f.write(str(i))
                    break
                f.write(f'{str(i)},')
                
        with open ('segundo.txt', self._metodo) as f:
            for i in range(50, 200+1):
                if(i == 200):
                    f.write(str(i))
                    break
                f.write(f'{str(i)},')



