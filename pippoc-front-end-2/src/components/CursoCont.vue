<template>
    Testeando la wea por la xuxa    
 
    <p v-for="elemento in nombre" :key="elemento.id">{{elemento.nombre}} </p>
</template>

<script>
import docData from 'http://localhost:8000/documentos'

export default{
    data(){
        return {nombre:docData}
    }
}
</script>