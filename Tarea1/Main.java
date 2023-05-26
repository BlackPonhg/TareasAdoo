public class Main {
    public static void main(String[] args) {
        Perro firulais = new Perro();
        Vaca v = new Vaca();
        Gato g = new Gato();
        Animal[] Animales = new Animal[]{firulais,v,g};
        for (Animal a: Animales) {
            a.Ruido();
        }
    }
}