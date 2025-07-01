[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/IOxRa_w9)

# Trabajo Práctico N° 4: Ciclo de vida de un componente

En este trabajo vamos a repasar los temas vistos en la clase sobre el ciclo de vida de un componente.  
Debemos crear un componente llamado `Alertas`.

## Componente Lista
Crear un componente llamado `Lista` que renderice una lista de elementos (provista en la carpeta `resources`).  
La lista debe cargarse dentro del hook `onMounted`. Para simular una demora en la carga, podemos utilizar el método `setTimeout`, que permite ejecutar una función luego de un tiempo determinado (en milisegundos).

```javascript
setTimeout(() => {
  // acción a ejecutar luego de 3 segundos
}, 3000);
```

Esta función ejecutará una acción **después de 3 segundos**.

---

## Componente Tareas
Crear un componente llamado `Tareas`, el cual debe contener una lista de tareas a las que podamos **agregar nuevas**.  
En este componente deben utilizarse los hooks `onBeforeUpdate` y `onUpdated`, mostrando en consola los siguientes mensajes:
- En `onBeforeUpdate`: **"Lista aún no modificada"**
- En `onUpdated`: **"Lista modificada"**

Además, se debe **pintar de algun color a elección** los ítems que existían **antes** de la modificación.

---

## Componente DimensionComponente
Crear un componente llamado `DimensionComponente`, que mostrará un título con las dimensiones del componente.  
Para esto debemos **escuchar eventos**, los cuales deben agregarse en el hook `onMounted` y removerse en el hook `onUnmounted`.

> En este caso, escucharemos el evento `resize` del elemento `window`.
Recuerden que cuando escuchamos podemos pasar una función al evento 

---

## Integración de los componentes
Para mostrar estos tres componentes ( `Lista`, `Tareas`, `DimensionComponente`) deben llamarse **dinámicamente**, como lo aprendimos en clase.  
La forma de selección es libre: pueden usar **tags**, **botones**, **select**, etc.

---


