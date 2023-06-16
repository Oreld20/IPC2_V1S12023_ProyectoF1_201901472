
class Pelicula:
    def __init__(self, categoria, titulo, director, anio, fecha, hora):
        self.categoria = categoria
        self.titulo = titulo
        self.director = director
        self.anio = anio
        self.fecha = fecha
        self.hora = hora

    def imprimir_categoria(self):
        print(f"categoria: {self.categoria}, titulo: {self.titulo}, director: {self.director}, anio: {self.anio}, fecha: {self.fecha}, hora: {self.hora}")

    def imprimir_pelicula(self):
        print(f"titulo: {self.titulo}, director: {self.director}")

