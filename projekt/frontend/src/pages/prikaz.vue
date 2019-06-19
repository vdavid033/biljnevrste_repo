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
Uporabni dio:
<div v-for="dio in vrsta.uporabni_dio" :key="dio.id" class="q-my-sm" clickable v-ripple>
  <div v-for="udio in uporabni_dio" :key="udio.id">
    <span v-if="dio === udio.url" >
        {{ udio.naziv }}
    </span>
  </div>
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

  <div v-for="slika1 in vrsta.slika" :key="slika1.id" class="q-my-sm" clickable v-ripple>
    <div v-for="uslika in slika" :key="uslika.id">
      <div v-if="slika1 === uslika.url" >
      <img :src=uslika.naziv_slike  />
                {{ uslika.opis_slike }}
      </div>
    </div>
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
      slide: '1',
      vrsta: '',
      varijet: '',
      uporabni_dio: [],
      slika: []

    }
  },
  created () {
    this.fetchBiljneVrste()
    this.fetchVarijet()
    this.fetchUporabniDio()
    this.fetchSlike()
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
    fetchUporabniDio () {
      this.$axios.get('http://193.198.97.14:8000/api/uporabnidijelovi/?format=json')
        .then((response) => {
          this.uporabni_dio = response.data
        })
        .catch(() => {
          this.$q.notify({
            message: 'Loading failed'
          })
        })
    },
    fetchSlike () {
      this.$axios.get('http://193.198.97.14:8000/api/slike/?format=json')
        .then((response) => {
          this.slika = response.data
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
