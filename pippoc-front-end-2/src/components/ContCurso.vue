<template>
    <v-card variant="ourlined">
        <div class="mt-2 ml-4 mb-2">
            <v-btn @click="new_tab">
                Agregar Unidad
            </v-btn>
        </div>
        
        <v-tabs
            v-model="tab"
            bg-color="indigo"
        >
            <v-tab v-for="(item, i) in items" :value="i"> {{ item }} </v-tab>
        </v-tabs>
    
        <v-card-text>
            <v-window v-model="tab">
            <v-window-item v-for="(item, i) in items" :value="i">
                <v-card variant="outlined">
                    <h2>Unidad {{ i+1 }}: Sección 1</h2>

                    <v-checkbox color="indigo" v-for="(item,j) in elementos" >
                        <template v-slot:label>
                            <div>
                                <v-row class="justified-center align-center">
                                    <h3><v-icon>mdi-file</v-icon> {{ item }} </h3>
                                    <v-btn class="ml-4" width="100" :href="links[j]" >Ver</v-btn>
                                </v-row>
                            </div>
                        </template>
                    </v-checkbox>

                    <div class="ma-3">
                        <v-row class="ma-3">
                            <v-btn @click="DocList = !DocList">Agregar elemento</v-btn>
                            <DocList v-model="DocList" :docs="documentos" :elementos="elementos" :archivos="archivos" :links="links"/>
                            <v-btn @click="FileUploader = !FileUploader" class="ml-2"> Subir archivo</v-btn>
                            <FileUploader v-model="FileUploader"/>
                        </v-row>
                    </div>
                </v-card>

                <v-divider></v-divider>

                <v-card variant="outlined">
                    <h2>Unidad {{ i+1 }}: Sección 2</h2>
                    <v-checkbox color="indigo">
                        <template v-slot:label><div>
                            <h3><v-icon>mdi-note-edit</v-icon> Prueba {{ i+1 }} </h3>
                        </div></template>
                    </v-checkbox>
                </v-card>
            </v-window-item>
            </v-window>
        </v-card-text>


      


    </v-card>
  </template>
  
<script>
import { getDocumentos } from '@/axios/documentosAxios';
import FileUploader from '@/components/displays/FileUploader.vue'
import DocList from '@/components/displays/DocList.vue'

export default {
  data() {
    return {
      documentos: [],
      formatos: [],
      archivos: [],
      tab: null,
      items: ["Unidad 1", "Unidad 2", "Unidad 3"], // Add a tab property for v-model,
      titulo:null,
      elementos: [],
      links: [],
      FileUploader: false,
      DocList: false
    };
  },
  components:{
    FileUploader,
    DocList
  },
  methods:{
    new_tab(){
        const r = /(\d+)/;
        const last_item = this.items.slice(-1)[0]
        const next_unit = parseInt(last_item.match(r)[0]) + 1
        const new_item = "Unidad " + String(next_unit)
        this.items.push(new_item)
    }
  },
  created() {
    // Fetch documentos from Django backend using the imported function
    getDocumentos()
      .then(data => {
        this.documentos = data.map(function(doc){
            return doc.nombre
        })
        this.formatos = data.map(function(doc){
            return doc.formato
        })
        this.archivos = data.map(function(doc){
            return doc.archivo
        })
        // Do any additional processing with documentos if needed
      })
      .catch(error => {
        // Handle error if needed
      });
  },
  updated(){
    getDocumentos()
      .then(data => {
        this.documentos = data.map(function(doc){
            return doc.nombre
        })
        this.formatos = data.map(function(doc){
            return doc.formato
        })
        this.archivos = data.map(function(doc){
            return doc.archivo
        })
        // Do any additional processing with documentos if needed
      })
      .catch(error => {
        // Handle error if needed
      });
  }

  // Other methods and component logic
};
</script>
