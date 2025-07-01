import { createWebHistory, createRouter } from 'vue-router'
import AboutView from '../views/AboutView.vue'
import ContactView from '../views/ContactView.vue'
import ProductView from '../views/ProductView.vue'

const routes = [
  {
    path: '/',
    name: 'sobre-nosotros',
    component: AboutView
  },
  {
    path: '/contacto',
    name: 'contacto',
    component: ContactView
  },
  {
    path: '/producto',
    name: 'producto',
    component: ProductView
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
