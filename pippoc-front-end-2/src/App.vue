<script setup>
import { ref, computed } from 'vue'
import Home from './views/HelloWorld.vue'
import VistaCurso from './views/VistaCurso.vue'
import VistaHome from './views/VistaHome.vue'

const routes = {
  '/': Home,
  '/curso': VistaCurso,
  '/home': VistaHome
}

const currentPath = ref(window.location.hash)

window.addEventListener('hashchange', () => {
  currentPath.value = window.location.hash
})

const currentView = computed(() => {
  return routes[currentPath.value.slice(1) || '/'] || NotFound
})
</script>

<template>
  <a href="#/home">VistaHome</a> |
  <a href="#/curso">VistaCurso</a>
  <component :is="currentView" />
</template>