<template>
    <v-card
    title="Cuso Prevención de Riesgos"
    subtitle="Pueblo Minera"
    text="Curso de Prevención de Riesgos diseñada para la minera 'Pueblo Minera'"
    variant="outlined"
    prepend-icon="mdi-home"
    >
        <v-card-actions>
            <v-lists>
                <h1><v-icon>mdi-file-outline</v-icon> Reglamento del Curso </h1>
                <h1><v-icon>mdi-folder</v-icon> Carpeta Genera del Curso </h1>
                <h1><v-icon>mdi-file-outline</v-icon> Planificación General del Curso </h1>
            </v-lists>

        </v-card-actions>
    </v-card>
    <v-divider></v-divider>
</template>

<script>
  import { getCursos } from '../axios/cursosAxios';
  import { getParticipantes } from '../axios/participantesAxios';
  
  export default {
    data() {
      return {
        cursos: [],
        participantes: [],
      };
    },
    mounted() {
      // Fetch cursos from Django backend using the imported function
      getCursos()
        .then(data => {
          this.cursos = data;
          // After fetching cursos, fetch participantes
          return getParticipantes();
        })
        .then(data => {
          this.participantes = data;
        })
        .catch(error => {
          // Handle error if needed
        });
    },
    // Other methods and component logic
  };
  </script>
  