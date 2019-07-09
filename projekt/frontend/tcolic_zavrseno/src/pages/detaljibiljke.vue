<template>

    <div class="q-pa-md">

    <div class="row">
      <div class="col-4">
         <div class="container">
         <div v-for="slika1 in vrsta.slika" :key="slika1.id" class="image" clickable v-ripple>
    <div v-for="uslika in slika" :key="uslika.id">
      <div v-if="slika1 === uslika.url" >
          <img :src=uslika.naziv_slike  />
          <div class="middle">
               <div class="text"> {{ uslika.opis_slike }} </div>
          </div>
      </div>
    </div>
  </div>
     </div>
      </div>
      <div class="col-8">
        <div class="q-pa-md">

        <div class="row">
        <div class="col">
            <div class="tekst">
        HRVATSKI NAZIV: </div> {{ vrsta.hrvatski_naziv_vrste }} &emsp; &emsp; &emsp; &nbsp;
        <div></div>
        <div class="tekst">LATINSKI NAZIV: </div>{{ vrsta.latinski_naziv }}
        <div>&nbsp;</div>
            <div></div>
        <div class="tekst"> SINONIM: </div> {{ vrsta.sinonim_vrste }}
        </div>
        <div class="col">
            <div class="tekst">VARIJETET: </div>{{ varijet.naziv_varijeta }}
        <div>&nbsp;</div>
            <div>
        <div class="tekst">UPORABNI DIO:</div>
        <div v-for="dio in vrsta.uporabni_dio" :key="dio.id" class="q-my-sm" clickable v-ripple>
        <div v-for="udio in uporabni_dio" :key="udio.id">
            <span v-if="dio === udio.url" >
                {{ udio.naziv }}
            </span>
        </div>
        </div>
        </div>
        <div>&nbsp;</div>
        </div>
        </div>
    </div>
        <div class="row" style="margin-left: 1.3%;">
        <div class="tekst"> OPIS BILJKE: </div>
        <div>
            <div class="layout-padding">
            {{ vrsta.opis_vrste }}
            </div>
        </div>
        </div>
        <div class="row" style="justify-content: flex-end;">
        <div>
            <q-btn color="green" text-color="black" class="absolute" style="right: 0; right: 200px; transform: translateY(50%);" label="Izbriši" />
            <q-btn color="green" text-color="black" class="absolute" style="right: 0; right: 100px; transform: translateY(50%);" label="Uredi" />
            </div>
      </div>
      </div>
    </div>
     </div>
</template>

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
