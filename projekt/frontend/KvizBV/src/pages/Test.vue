<template>
  <q-page padding>
    <div>
      {{ this.biljka.hrvatski_naziv_vrste }}
    </div>
    <div class="q-pa-lg text-weight-bold q-display-2">
      Hrvatski Naziv
    </div>
    <div class="row">
      <div class="collumn">
        <div>
          <img alt="Quasar logo" src="~assets/quasar-logo-full.svg">
        </div>
        <div>
          <q-radio v-model="radioS" val="Izbor 1" />
        </div>
      </div>
      <div class="collumn">
        <div>
          <img alt="Quasar logo" src="~assets/quasar-logo-full.svg">
        </div>
        <div>
          <q-radio v-model="radioS" val="Izbor 2" />
        </div>
      </div>
      <div class="collumn">
        <div>
          <img alt="Quasar logo" src="~assets/quasar-logo-full.svg">
        </div>
        <div>
          <q-radio v-model="radioS" val="Izbor 3" />
        </div>
      </div>
      <div class="collumn">
        <div>
          <img alt="Quasar logo" src="~assets/quasar-logo-full.svg">
        </div>
        <div>
          <q-radio v-model="radioS" val="Izbor 4"/>
        </div>
      </div>
      <div class="collumn">
        <div>
          <img alt="Quasar logo" src="~assets/quasar-logo-full.svg">
        </div>
        <div>
          <q-radio v-model="radioS" val="Izbor 5"/>
        </div>
      </div>
    </div>
    <div class="q-pa-lg">
      <q-expansion-item
        expand-separator
        label="Latinski naziv"
        caption="Latinski naziv"
      >
        <q-list bordered padding class="rounded-borders">
        <q-item-label header>Izaberi naziv</q-item-label>
        <q-item v-for="vrsta in biljnevrste" :key="vrsta.id" class="q-my-sm" clickable v-ripple>
          <q-item-section>
            <q-radio v-model="radioV" :val=vrsta.latinski_naziv />
          </q-item-section>
          <q-item-section>
            <q-item-label>
              <a :href=vrsta.url>
              {{ vrsta.latinski_naziv }}
              </a>
            </q-item-label>
          </q-item-section>
        </q-item>
        </q-list>
      </q-expansion-item>
    </div>
    <div class="q-pa-lg row">
      <div class="col">
        <q-list bordered padding class="rounded-borders" >
        <q-item-label header>Uporabni dio</q-item-label>
        <q-item  v-for="dio in uporabnidijelovi" :key="dio.id" class="q-my-sm" clickable v-ripple>
          <q-item-section>
            <q-checkbox v-model="checkUD" :val=dio.naziv color="teal" />
          </q-item-section>
          <q-item-section>
            <q-item-label title>{{ dio.naziv }}</q-item-label>
          </q-item-section>
        </q-item>
        </q-list>
      </div>
    </div>
    <div class="q-pa-lg right">
      <q-btn @click="provjeri" color="blue" text-color="white" label="Provjeri" />
      <q-btn @click="randomLink" :to="kvizLink" color="green" text-color="white" label="Novo pitanje" />
    </div>
  </q-page>
</template>

<style>
</style>

<script>
export default {
  data () {
    return {
      links: ['kviz1', 'kviz2'],
      kvizLink: 'kviz1',
      hrvatskiNaziv: '',
      radioS: '',
      radioR: '',
      radioV: '',
      radioB: '',
      checkUD: [],
      textLN: '',
      textHN: '',
      rodovi: [],
      biljnevrste: [],
      uporabnidijelovi: [],
      biljka: []
    }
  },
  created () {
    this.fetchRodovi()
    this.fetchBiljneVrste()
    this.fetchUporabniDijelovi()
  },
  methods: {
    provjeri () {
    },
    fetchRodovi () {
      this.$axios.get('http://193.198.97.14:8000/api/rodovi/?format=json')
        .then((response) => {
          this.rodovi = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },
    fetchBiljneVrste () {
      this.$axios.get('http://193.198.97.14:8000/api/biljnevrste/?format=json')
        .then((response) => {
          this.biljnevrste = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },
    randomBiljka () {
      this.biljka = this.biljnevrste[Math.floor(Math.random() * this.biljnevrste.length)]
    },
    fetchUporabniDijelovi () {
      this.$axios.get('http://193.198.97.14:8000/api/uporabnidijelovi/?format=json')
        .then((response) => {
          this.uporabnidijelovi = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  randomLink (e, go) {
    e.navigate = false
    // this.kvizLink = this.links[Math.floor(Math.random() * 2)]
    setTimeout(() => {
      go()
    }, 1)
  }
}
</script>
