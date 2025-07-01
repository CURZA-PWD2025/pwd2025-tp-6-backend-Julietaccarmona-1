
# TRABAJO PRÁCTICO N.º 3  
## VUE-ROUTER

### Consigna 🚀

Vamos a crear tres componentes para nuestras **vistas**. Recuerden que, para organizar nuestro proyecto, cada tipo de componente debe estar agrupado por tipo. Si bien esto no es obligatorio, es una buena práctica.  
Crearemos dentro de la carpeta `src` la carpeta que contendrá nuestras `views`, así que la llamaremos de igual manera: `views`.

#### COMPONENTES `views` 👁️

Crear los componentes `ProductView`, `AboutView` y `ContactView`. Para los componentes `About` y `Contact`, generen contenido libremente.

#### COMPONENTES `components` o componentes de aplicación

Ahora vamos a crear nuestros componentes de aplicación: 📦  
- `ProductList`: el cual tendrá una lista de `productos`, en este caso **zapatillas**.  
- `ItemList`: este componente se encargará de mostrar los datos de cada producto.

### Creando las rutas con Vue Router 🔄

Primero debemos ejecutar el siguiente comando:
```bash
npm install vue-router@4
```
Así tendremos el enrutador instalado en nuestra aplicación.

**Crear la carpeta** `routes` en la raíz del proyecto. Dentro de dicha carpeta, crear el archivo `router.ts` y definir las rutas que vamos a utilizar en nuestro proyecto.

```ts
import { createWebHistory, createRouter } from 'vue-router'

const routes = [...]

export default const router = createRouter({
    history: createWebHistory(),
    routes // recuerden que al llamarse igual que el atributo, no es necesario definir el valor de esta forma: routes: routes
})
```

#### Configurar el archivo `main.ts`

Para que **Vue** tome las rutas, debemos **usar** el enrutador. Para ello, tendremos que agregarlo de la siguiente manera:

```ts
import router from './routes/router.ts'
createApp(App)
  .use(router)
  .mount('#app')
```

### Creando el menú de navegación 👨‍✈️

En `App.vue` crearemos un menú de navegación entre componentes.  
Recuerden que vamos a usar `<Router-link to="">` para los enlaces y `<Router-View/>` para mostrar el contenido.

### No olvidar 🧠  
- Como en los trabajos anteriores, pueden estilizar sus componentes.  
- En la carpeta `resources` les dejo los archivos que usaremos en nuestra aplicación. Para este **TP**, los archivos de las imágenes serán **locales**. Esto quiere decir que no serán enlaces a imágenes externas, sino que las tendremos en nuestro proyecto.  
- La carpeta `imgs` debe ir dentro de la carpeta `public`. **VUEJS** reconoce esta carpeta como origen para los recursos (elementos que son para los usuarios finales), por lo que podemos acceder fácilmente, de esta manera, por ejemplo:

```html
<img src="imgs/nombre.extension" />
```

En nuestro caso, al ser elementos dinámicos, vamos a tener que hacer algo así:

```html
<img :src="'/imgs/' + producto.imagen" />
```
