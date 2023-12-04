public class Islas {
    public int contarIslas(char[][] matriz) {
        if (matriz == null || matriz.length == 0 || matriz[0].length == 0) {
            return 0;
        }

        int filas = matriz.length;
        int columnas = matriz[0].length;
        int contadorIslas = 0;

        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columnas; j++) {
                if (matriz[i][j] == '1') {
                    contadorIslas++;
                    explorarYMarcarIsla(matriz, i, j);
                }
            }
        }

        return contadorIslas;
    }

    private void explorarYMarcarIsla(char[][] matriz, int i, int j) {
        int filas = matriz.length;
        int columnas = matriz[0].length;

        if (i < 0 || i >= filas || j < 0 || j >= columnas || matriz[i][j] == '0') {
            return;
        }

        matriz[i][j] = '0'; // Marcar como visitado

        // Explorar en todas las direcciones
        explorarYMarcarIsla(matriz, i + 1, j);
        explorarYMarcarIsla(matriz, i - 1, j);
        explorarYMarcarIsla(matriz, i, j + 1);
        explorarYMarcarIsla(matriz, i, j - 1);
    }

    public static void main(String[] args) {
        char[][] matriz = {
                {'0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',},
                {'0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',},
                {'0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',},
                {'0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',},
                {'0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',},
                {'0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',},
                {'0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',},
                {'0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',},
                {'0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',},
                {'0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',},
                {'0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',},
                {'0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',},
                {'0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',},
                {'0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',},
                {'0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',},
                {'0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',},
                {'0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',},
                {'0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',},
                {'0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',},
                {'0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',},
                {'0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',},
                {'0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',}
        };

        Islas contador = new Islas();
        int numeroIslas = contador.contarIslas(matriz);

        System.out.println("Número de islas: " + numeroIslas);
    }
}
