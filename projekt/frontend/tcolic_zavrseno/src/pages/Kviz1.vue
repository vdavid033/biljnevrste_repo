<template>
  <q-page padding>
    <div>
      naziv: {{ this.biljka.hrvatski_naziv_vrste }}
    </div>
    <div>
          <q-img
            alt="slikaBiljke"
            :src="slika1url"
            spinner-color="white"
            style="height: 400px; width: 400px; border-radius: 50%"
          />
    </div>
    <div class="q-pa-lg">
      <q-expansion-item
        expand-separator
        label="Hrvatski naziv"
        caption="Hrvatski naziv"
      >
        <q-list bordered padding class="rounded-borders">
        <q-item-label header>Izaberi naziv</q-item-label>
        <q-item @click="promjeniNaslovHrvatskiNaziv(val)" v-for="vrsta in biljnevrste" :key="vrsta.id" class="q-my-sm" clickable v-ripple>
          <q-item-section>
            <q-radio v-model="radioHrvatskiNaziv" :val=vrsta.hrvatski_naziv_vrste />
          </q-item-section>
          <q-item-section>
            <q-item-label>
              <a :href=vrsta.url>
              {{ vrsta.hrvatski_naziv_vrste }}
              </a>
            </q-item-label>
          </q-item-section>
        </q-item>
        </q-list>
      </q-expansion-item>
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
            <q-radio v-model="radioLatinskiNaziv" :val=vrsta.latinski_naziv />
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
      kvizLink: 'kviz2',
      hrvatskiNaziv: '',
      radioHrvatskiNaziv: '',
      radioLatinskiNaziv: '',
      checkUD: [],
      textLN: '',
      textHN: '',
      rodovi: [],
      biljnevrste: [],
      uporabnidijelovi: [],
      biljka: {},
      slika1url: ''
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
          this.biljka = this.biljnevrste[Math.floor(Math.random() * this.biljnevrste.length)]
          // console.log(this.biljka)
          this.$axios.get(this.biljka.slika[Math.floor(Math.random() * this.biljka.slika.length)])
            .then((response) => {
              this.slika1url = response.data.naziv_slike
            })
            .catch(error => {
              console.log(error)
            })
        })
        .catch(error => {
          console.log(error)
        })
    },
    fetchUporabniDijelovi () {
      this.$axios.get('http://193.198.97.14:8000/api/uporabnidijelovi/?format=json')
        .then((response) => {
          this.uporabnidijelovi = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },
    randomLink (e, go) {
      e.navigate = false
      this.kvizLink = this.links[Math.floor(Math.random() * 2)]
      setTimeout(() => {
        if (this.kvizLink === 'kviz1') {
          window.location.reload()
        } else {
          go()
        }
      }, 1)
    }
  }
}
</script>
