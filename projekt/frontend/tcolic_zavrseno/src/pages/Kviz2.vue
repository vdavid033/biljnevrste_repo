<template>
  <q-page padding>
    <div class="q-pa-lg text-weight-bold text-h3 q-display-2">
      Biljna vrsta: {{ this.biljka.hrvatski_naziv_vrste }}
    </div>
    <div class="row">
      <div class="collumn">
        <div>
          <q-img
            alt="slikaBiljke"
            :src="slikeIzbor[0]"
            spinner-color="white"
            style="height: 250px; width: 250px; border-radius: 50%"
          />
        </div>
        <div>
          <q-radio v-model="radioSlike" val="Izbor 1" />
        </div>
      </div>
      <div class="collumn">
        <div>
          <q-img
            alt="slikaBiljke"
            :src="slikeIzbor[1]"
            spinner-color="white"
            style="height: 250px; width: 250px; border-radius: 50%"
          />
        </div>
        <div>
          <q-radio v-model="radioSlike" val="Izbor 2" />
        </div>
      </div>
      <div class="collumn">
        <div>
          <q-img
            alt="slikaBiljke"
            :src="slikeIzbor[2]"
            spinner-color="white"
            style="height: 250px; width: 250px; border-radius: 50%"
          />
        </div>
        <div>
          <q-radio v-model="radioSlike" val="Izbor 3" />
        </div>
      </div>
      <div class="collumn">
        <div>
          <q-img
            alt="slikaBiljke"
            :src="slikeIzbor[3]"
            spinner-color="white"
            style="height: 250px; width: 250px; border-radius: 50%"
          />
        </div>
        <div>
          <q-radio v-model="radioSlike" val="Izbor 4"/>
        </div>
      </div>
      <div class="collumn">
        <div>
          <q-img
            alt="slikaBiljke"
            :src="slikeIzbor[4]"
            spinner-color="white"
            style="height: 250px; width: 250px; border-radius: 50%"
          />
        </div>
        <div>
          <q-radio v-model="radioSlike" val="Izbor 5"/>
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
        <q-item-label header>Izaberi latinski naziv</q-item-label>
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
      kvizLink: 'kviz1',
      hrvatskiNaziv: '',
      radioSlike: '',
      radioLatinskiNaziv: '',
      checkUD: [],
      textLN: '',
      textHN: '',
      rodovi: [],
      biljnevrste: [],
      uporabnidijelovi: [],
      biljka: {},
      slikeIzbor: [],
      sveSlike: []
    }
  },
  created () {
    this.fetchRodovi()
    this.fetchBiljneVrste()
    this.fetchUporabniDijelovi()
    this.fetchRandomSlike()
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
          this.$axios.get(this.biljka.slika[Math.floor(Math.random() * this.biljka.slika.length)])
            .then((response) => {
              this.slikeIzbor.push(response.data.naziv_slike)
              console.log(response)
            })
            .catch(error => {
              console.log(error)
            })
        })
        .catch(error => {
          console.log(error)
        })
    },
    fetchRandomSlike () {
      this.$axios.get('http://193.198.97.14:8000/api/slike/?format=json')
        .then((response) => {
          this.sveSlike = response.data
          for (let i = 0; i < 4;) {
            var randomSlika = Math.floor(Math.random() * this.sveSlike.length)
            if (this.slikeIzbor.includes(this.sveSlike[randomSlika].naziv_slike) === false) {
              this.slikeIzbor.push(this.sveSlike[randomSlika].naziv_slike)
              console.log(this.slikeIzbor)
              i++
            }
          }
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
    }
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
</script>
