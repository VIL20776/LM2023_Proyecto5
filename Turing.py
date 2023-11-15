from time import sleep

R = 1
L = -1

class TuringMachine:
    
    def __init__(self,
        Q: set, E: set, G: set, d: dict, 
        q_0: str, q_a: str, q_r: str):
        """
        Q: Conjunto de estados.
        E: Alfabeto de entrada.
        G: Alfabeto de cinta.
        d: Funcion de transicion.
        q_0: Estado inicial.
        q_a: Estado de aceptacion.
        q_r: Estado de rechazo.
        """
        self.Q = Q
        self.E = E
        self.G = G
        self.d = d
        self.q_0 = q_0
        self.q_a = q_a
        self.q_r = q_r
    
    def execute(self, w: str):
        """
        Recibe una cadena de entrada y genera una cadena de salida.
        w: cadena de entrada
        """
        
        # Previene cadenas invalidas
        if any(e not in self.G for e in w):
            print("Error: Cadena invalida.")
            return 1
        
        C_string = self.q_0 + w + '_'
        C = list(C_string) 
        
        print(f"Configuracion 1: {C_string}") # Configuracion inicial

        n = 1
        i = 0
        while (self.q_a not in C) and (self.q_r not in C):
            state, symbol, move = self.d[(C[i], C[i+1])]
            
            C[i+1] = symbol if symbol != '' else C[i+1]
            C[i] = C[i+move]
            C[i+move] = state
            i += move
            
            if i < 0: i = 0
            
            if i >= len(C)-1: C.append('_')

            n += 1
            C_string = "".join(C)
            print(f"Configuracion {n}: {C_string}") # Imprime configuracion n
            
            sleep(0.5)
        
        C_string = "".join(C)
        print(f"\nConfiguacion final de la cinta: {C_string}")
        if self.q_a in C:
            print("Se llego a un estado de aceptacion.")
        elif self.q_r in C:
            print("Se llego a un estado de rechazo.")
        else:
            print("Bucle infinito. Se detuvo la ejecucion.")
        
        
        

        