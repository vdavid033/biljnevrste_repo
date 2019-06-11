<template>
 <q-page padding="">
<div>
Hrvatski naziv: {{ vrsta.hrvatski_naziv_vrste }} &emsp; &emsp; &emsp; &nbsp;
Sinonim: {{ vrsta.sinonim_vrste }}
  </div>
  <div></div>
  <div>
Latinski naziv: {{ vrsta.latinski_naziv }}
  </div>
   <div>&nbsp;</div>
    <div>
Varijet: {{ varijet.naziv_varijeta }}
  </div>
   <div>&nbsp;</div>
    <div>
Uporabni dio: {{ vrsta.uporabni_dio }}
<div v-for="dio in vrsta.uporabni_dio" :key="dio.id" class="q-my-sm" clickable v-ripple>
  {{ dio.naziv }}
  </div>
  </div>
   <div>&nbsp;</div>
    <div>
OPIS BILJKE:
  </div>
  <div>
    <div class="layout-padding">
      {{ vrsta.opis_vrste }}
    </div>
  </div>
  <div class="q-pa-md">
    <q-carousel
      animated
      v-model="slide"
      arrows
      navigation
      infinite
    >
      <q-carousel-slide :name="1" img-src="https://www.veleri.hr/studisweb/images/veleri_back.png" />
      <q-carousel-slide :name="2" img-src="https://www.veleri.hr/studisweb/images/veleri_back.png" />
      <q-carousel-slide :name="3" img-src="https://cdn.quasar.dev/img/parallax2.jpg" />
      <q-carousel-slide :name="4" img-src="https://cdn.quasar.dev/img/quasar.jpg" />
    </q-carousel>
  </div>
  <div>
     <q-btn color="blue" text-color="black" class="absolute" style="right: 0; right: 200px; transform: translateY(50%);" label="Izbriši" />
      <q-btn color="blue" text-color="black" class="absolute" style="right: 0; right: 100px; transform: translateY(50%);" label="Uredi" />
    </div>
  </q-page>
</template>

<style>

</style>

<script>
export default {
  data () {
    return {
      posts: [],
      current: 3,
      slide: 1,
      vrsta: '',
      varijet: '',
      uporabni_dio: []
    }
  },
  created () {
    this.fetchBiljneVrste()
    this.fetchVarijet()
    this.fetchUporabniDio()
  },
  methods: {
    fetchVarijet () {
      this.$axios.get('http://193.198.97.14:8000/api/varijeti/3/?format=json')
        .then((response) => {
          this.varijet = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },
    fetchBiljneVrste () {
      this.$axios.get('http://193.198.97.14:8000/api/biljnevrste/3/?format=json')
        .then((response) => {
          this.vrsta = response.data
          // fetchUporabniDio(this.vrsta.uporabni_dio)
        })
        .catch(() => {
          this.$q.notify({
            message: 'Loading failed'
          })
        })
    },
    fetchUporabniDio (dio) {
      this.$axios.get(dio)
        .then((response) => {
          this.uporabni_dio = response.data
        })
        .catch(() => {
          this.$q.notify({
            message: 'Loading failed'
          })
        })
    }
  }
}

</script>
