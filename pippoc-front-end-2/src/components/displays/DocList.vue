<template>
    <v-dialog>
        <div justify="center" align="center">
            <v-card title="Agregar elemento" max-height="500" max-width="800">
                <div class="ma-5">    
                    <v-text-field label="Nombre del elemento" v-model="nombre"></v-text-field>
                    <v-select
                        label="Seleccione documento"
                        :items="items"
                        item-title="doc"
                        item-value="archivo"
                        v-model="link"
                    >
                    </v-select>
                    <v-btn @click ="insertar"> 
                        Subir
                    </v-btn>
                </div>
            </v-card>
        </div>
    </v-dialog>
</template>

<script>
    export default{
        name: "DocElement",
        props: {
            "docs" : Array,
            "archivos" : Array, 
            "elementos" : Array,
            "links" : Array,
        },
        data() {
            return {
                items: [],
                nombre: null,
                link: null
            }
        },
        mounted(){
            this.$nextTick(() =>{
                let i=0
                while(i<this.$props.docs.length){
                    let item = {
                        "doc" : this.$props.docs[i],
                        "archivo" : this.$props.archivos[i]
                    }
                    this.items.push(item)
                    i = i + 1
                }
                console.log(this.items)
                }
            )
        },
        methods:{
            insertar(){
                this.$props.elementos.push(this.nombre)
                console.log(this.link)
                this.$props.links.push(this.link)
            }
        }
    }
</script>