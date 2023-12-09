<template>
    <v-card title="Salida de Chat" variant="tonal">
        <v-card>
            Aqui se debe ir cambiando el texto
        </v-card>
        <v-text-field label="¿Que deseas de la IA?" variant="solo-inverted" v-model="mensaje"></v-text-field>
        <v-btn @click="submit"> <v-icon>mdi-send</v-icon>  Enviar</v-btn>
    </v-card>
    
</template>


<script>
export default{
    data(){
        return{
            mensaje: null
        }
    },
    methods:{
        submit(){
            console.log(this.mensaje)
        }
    }
}
</script>