using Microsoft.AspNetCore.Mvc;
using TresEnRaya.Models;

namespace TresEnRaya.Controllers
{
    public class JuegoController : Controller
    {
        private static Juego juego = new Juego();

        public IActionResult Tablero()
        {
            return View(juego);
        }

        [HttpPost]
        public IActionResult Marcar(int fila, int columna)
        {
            juego.MarcarCasilla(fila, columna);
            return RedirectToAction("Tablero");
        }

        public IActionResult Reiniciar()
        {
            juego.ReiniciarTablero();
            return RedirectToAction("Tablero");
        }
    }
}
