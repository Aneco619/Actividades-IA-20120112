public class Josephus {
    
    public static int encontrarPosicionJosephus(int n) {
        // Verificar si n es una potencia de 2
        if ((n & (n - 1)) == 0) {
            // n es una potencia de 2, Josephus se sienta en la posición 1
            return 1;
        } else {
            // Calcular la posición según la fórmula
            return 2 * (n - Integer.highestOneBit(n)) + 1;
        }
    }

    public static void main(String[] args) {
        int numeroDeSoldados = 41;
        int josephusPosicion = encontrarPosicionJosephus(numeroDeSoldados);
        
        System.out.println("Josephus se sentó en la posición: " + josephusPosicion);
    }
}
