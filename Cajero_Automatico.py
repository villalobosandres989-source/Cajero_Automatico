
saldo = 1000
veces = int(input("Cuantas operaciones desea realizar: "))

for i in range (veces):

 def menu():
    
    print("=== Bienvenido al cajero automatico:) ===")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    
 menu()

 opcion = int(input("Escoga una opción: "))
    
 if opcion == 1:
        print("Su saldo es:", saldo)
        
 elif opcion == 2:
        monto = int(input("Cuanto desea retirar: "))
        saldo -= monto
        print("Retiro exitoso:), su nuevo saldo es:", saldo)

 elif opcion == 3:
    monto = int(input("Cuanto desesa depositar: "))
    saldo += monto
    print("Deposito exitoso:), su nuevo saldo es:", saldo)

 else:
    print("Por favor escoga una opción válida")        
        
