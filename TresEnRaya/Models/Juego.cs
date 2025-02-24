namespace TresEnRaya.Models
{
    public class Juego
    {
        public char[,] Tablero { get; set; } = new char[3, 3];
        public char TurnoActual { get; set; } = 'X';
        public char Ganador { get; private set; } = ' '; 

        public Juego()
        {
            ReiniciarTablero();
        }

        public void ReiniciarTablero()
        {
            for (int i = 0; i < 3; i++)
                for (int j = 0; j < 3; j++)
                    Tablero[i, j] = ' ';

            Ganador = ' '; // Reiniciar el ganador
        }

        public bool MarcarCasilla(int fila, int columna)
        {
            if (Tablero[fila, columna] == ' ' && Ganador == ' ') // Solo permitir jugadas si no hay ganador
            {
                Tablero[fila, columna] = TurnoActual;
                if (VerificarGanador())
                {
                    Ganador = TurnoActual;
                }
                else
                {
                    TurnoActual = (TurnoActual == 'X') ? 'O' : 'X';
                }
                return true;
            }
            return false;
        }

        private bool VerificarGanador()
        {
            char[] jugadores = { 'X', 'O' };
            foreach (var jugador in jugadores)
            {
                // Verificar filas y columnas
                for (int i = 0; i < 3; i++)
                {
                    if ((Tablero[i, 0] == jugador && Tablero[i, 1] == jugador && Tablero[i, 2] == jugador) ||
                        (Tablero[0, i] == jugador && Tablero[1, i] == jugador && Tablero[2, i] == jugador))
                    {
                        return true;
                    }
                }

                // Verificar diagonales
                if ((Tablero[0, 0] == jugador && Tablero[1, 1] == jugador && Tablero[2, 2] == jugador) ||
                    (Tablero[0, 2] == jugador && Tablero[1, 1] == jugador && Tablero[2, 0] == jugador))
                {
                    return true;
                }
            }

            return false;
        }
    }
}
