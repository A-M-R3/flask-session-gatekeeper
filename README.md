# Flask Session Gatekeeper

Un sistema ligero de gestión de estados y pasarela de acceso de usuarios desarrollado con Flask. Esta aplicación demuestra cómo mitigar la naturaleza sin estado (stateless) del protocolo HTTP mediante el uso de sesiones seguras cifradas, permitiendo un control de acceso condicional en tiempo real y renderizado dinámico de componentes de interfaz.

## Características Técnicas

* **Gestión de Estado Cifrada:** Implementación de cookies de sesión firmadas criptográficamente para persistir la identidad del usuario entre diferentes endpoints del servidor.
* **Filtro de Acceso Perimetral:** Validación condicional de credenciales de sesión activas para restringir el ingreso de usuarios anónimos a zonas de contenido privado.
* **Arquitectura de Plantillas Dinámicas:** Uso del motor de renderizado Jinja2 para alternar componentes visuales e inyectar variables de forma segura directamente desde el backend.
* **Interfaz de Estilo SaaS:** Diseño adaptativo, moderno y minimalista construido con HTML5 y CSS3 nativo, con soporte para transiciones suaves y estados de enfoque interactivos.

## Estructura de Componentes

* `app.py`: Núcleo de la aplicación. Gestiona el enrutamiento, los métodos de solicitud y las reglas de validación de la sesión.
* `templates/index.html`: Plantilla principal adaptativa que alterna layouts entre el formulario de acceso y la tarjeta de bienvenida.
* `templates/contenido.html`: Vista protegida que despliega el estado de los recursos del sistema según el nivel de autorización del usuario.
* `static/styles/home.css`: Hoja de estilos global que implementa la línea gráfica moderna del ecosistema.

## Despliegue Local

Para clonar y ejecutar este gateway de acceso en un entorno local, sigue los comandos detallados en tu terminal:

git clone https://github.com/TU_USUARIO/NUEVO_NOMBRE_REPOSITORIO.git
cd NUEVO_NOMBRE_REPOSITORIO
pip install Flask
python app.py

El servidor local se iniciará de forma automática en el puerto predeterminado.
