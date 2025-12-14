import torch

## Crear Tensor básico vacios
print("\n+ Crear tensores vacios.")

# list
t = torch.tensor([])
print(f"- Tensor básico inicializado con una lista vacia: {t}")

# tuple
t = torch.tensor(())
print(f"- Tensor básico inicializado con una tupla vacia: {t}")

# dict
# RuntimeError: Could not infer dtype of dict
# Se debe castear el tipo a otro para crear el tensor
t_list, t_tuple = torch.tensor(list({})), torch.tensor(tuple({}))
print(f"- Tensor básico inicializado con un diccionario vacio: \
      \n\tlist: {t_list} \
      \n\ttuple: {t_tuple}")


## Crear Tensor básico con datos
print("\n+ Crear Tensor con datos.")

# list
data = [1, 2, 3]
t = torch.tensor(data)
print(f"- Tensor básico con datos {data}: {t}")

# tuple
data = (1, 2, 3)
t = torch.tensor(data)
print(f"- Tensor básico con datos {data}: {t}")

# dict
# Pd.: sólo se utiliza las claves del diccionario en enteros, flotantes
#      o booleanos True=1 | False=0
data = {1: "1", 2: "2", 3: 3}
t = torch.tensor(list(data))
print(f"Tensor básico con datos list({data}): {t}")

t = torch.tensor(tuple(data))
print(f"Tensor básico con datos tuple({data}): {t}")



## Dimensiones
print("\n+ Dimensiones:")

# Tensor 0D
data = 5
t = torch.tensor(data)
print(f"- Tensor 0D: {t}, Dimensión: {t.dim()}")

# Tensor 1D
data = [1, 2, 3]
t = torch.tensor(data)
print(f"- Tesnor 0D {t}, dimensión: {t.dim()}")

# Tensor 2D
data = [[1, 2, 3], [4, 5, 6]]
t = torch.tensor(data)
print(f"- Tesnor 2D {t}, dimensión: {t.dim()}")

# Tensor 3D
data = [
        [
            [1, 2], [3, 4]
        ], 
        [
            [5, 6], [7, 8]
        ],
    ]
t = torch.tensor(data)
print(f"- Tesnor 3D {t}, dimensión: {t.dim()}")



## Atributos de tensores
## shape | dtype | device
data = [[1, 2, 3], [4, 5, 6]]
t = torch.tensor(data)
print(f"- Tesnor {t}, \
      \n\t- shape: {t.dim()}    \
      \n\t- dtype: {t.dtype}    \
      \n\t- device: {t.device}")
