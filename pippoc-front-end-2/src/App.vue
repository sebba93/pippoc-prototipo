<script setup>
import { ref, computed } from 'vue'
import VistaCurso from './views/VistaCurso.vue'
import VistaHome from './views/VistaHome.vue'
import HelloWorld from './views/HelloWorld.vue'

const routes = {
  '/curso': VistaCurso,
  '/': VistaHome,
  '/wip': HelloWorld
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
  <component :is="currentView" />
</template>