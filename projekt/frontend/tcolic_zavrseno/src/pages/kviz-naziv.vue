<template>
  <q-page padding>
    <div class="row" style="justify-content: center;">
      </div>
      <div class="q-pa-lg">
      <!--vd -->
      <!-- div class="col" -->
        <q-list bordered padding class="rounded-borders">
          <q-item-label header>Izaberi vrstu</q-item-label>
          <q-item v-for="value in biljnevrste" :key="value.id" class="q-my-sm" clickable v-ripple>
            <q-item-section>
              <q-radio v-model="radioV" :val=value.hrvatski_naziv_vrste />
            </q-item-section>
            <q-item-section style="float-left">
              <q-item-label>
                <a :href=value.url>
                {{ value.hrvatski_naziv_vrste }}
                </a>
              </q-item-label>
            </q-item-section>
            <q-item-section>
              <q-item-label>
                (lat. {{ value.latinski_naziv }})
              </q-item-label>
            </q-item-section>
            <span v-for="rod in rodovi" :key="rod.id">
              <div v-if="rod.url === value.ID_roda">
              <br />
              {{ rod.naziv_roda }}
              </div>
            </span>
            <span v-for="slika in slike" :key="slika.id">
              <span v-for="slika1 in value.slika" :key="slika1.id">
                <div v-if="slika.url === slika1" class="col-6">
                <br />
                <img :src=slika.naziv_slike style="width: 120px" />
                </div>
              </span>
            </span>
          </q-item>
        </q-list>
      </div>
    <div class="q-pa-lg">
      <q-input v-model="textLN" placeholder="Latinski naziv" />
    </div>
    <div class="q-pa-lg">
      <q-input v-model="textLN" placeholder="Botanička porodica" />
    </div>
    <div class="q-pa-lg row">
      <!--vd -->
      <div class="col">
        <q-list bordered padding class="rounded-borders" style="max-width: 400px">
        <q-item-label header>Izaberi rod</q-item-label>
        <q-item v-for="rod in rodovi" :key="rod.id" class="q-my-sm" clickable v-ripple>
          <q-item-section>
            <q-radio v-model="radioR" :val=rod.naziv_roda />
          </q-item-section>
          <q-item-section>
            <q-item-label>
              <a :href=rod.url>
              {{ rod.naziv_roda }}
              </a>
            </q-item-label>
          </q-item-section>
        </q-item>
        </q-list>
      </div>
        <div class="col">
        <q-list bordered padding class="rounded-borders" style="max-width: 400px">
        <q-item-label header>Izaberi vrstu</q-item-label>
        <q-item v-for="vrsta in biljnevrste" :key="vrsta.id" class="q-my-sm" clickable v-ripple>
          <q-item-section>
            <q-radio v-model="radioV" :val=vrsta.hrvatski_naziv_vrste />
          </q-item-section>
          <q-item-section>
            <q-item-label>
              <a :href=vrsta.url>
              {{ vrsta.hrvatski_naziv_vrste }}
              </a>
            </q-item-label>
          </q-item-section>
          <q-item-section>
            <q-item-label>
              (lat. {{ vrsta.latinski_naziv }})
            </q-item-label>
          </q-item-section>
        </q-item>
        </q-list>
      </div>
      <!-- end vd -->
    </div>
    <div class="q-pa-lg row">
      <div class="col">
        <q-list bordered padding class="rounded-borders" style="max-width: 400px">
        <q-item-label header>Uporabni dio</q-item-label>
        <q-item  v-for="dio in uporabnidijelovi" :key="dio.id" class="q-my-sm" clickable v-ripple>
          <q-item-section>
            <q-radio v-model='radioU' :val=dio.naziv />
          </q-item-section>
          <q-item-section>
            <q-item-label title>{{ dio.naziv }}</q-item-label>
          </q-item-section>
        </q-item>
        </q-list>
      </div>
      <div class="col">
        <q-list bordered padding class="rounded-borders" style="max-width: 400px">
          <q-item-label header>Bioaktivna tvar</q-item-label>
        <div class="q-gutter-sm">
              <q-checkbox v-model="izbor1" label="Izbor 1" />
            </div>
            <div class="q-gutter-sm">
              <q-checkbox v-model="izbor2" label="Izbor 2" />
            </div>
            <div class="q-gutter-sm">
              <q-checkbox v-model="izbor3" label="Izbor 3" />
            </div>
            <div class="q-gutter-sm">
              <q-checkbox v-model="izbor4" label="Izbor 4" />
            </div>
            <div class="q-gutter-sm">
              <q-checkbox v-model="izbor5" label="Izbor 5" />
            </div>
            <div class="q-gutter-sm">
              <q-checkbox v-model="izbor6" label="Izbor 6" />
            </div>
        </q-list>
      </div>
    </div>
    <div class="row" style="justify-content: flex-end;">
        <div class="q-pa-lg right" >
            <q-btn color="red" text-color="white" label="Završi" />
        </div>
        <div class="q-pa-lg right">
            <q-btn color="blue" text-color="white" label="Provjeri" />
        </div>
        <div class="q-pa-lg right">
            <q-btn @click="randomLink" :to="kvizLink" color="green" text-color="white" label="Novo pitanje" />
        </div>
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
      radioU: '',
      radioB: '',
      textLN: '',
      rodovi: [],
      biljnevrste: [],
      uporabnidijelovi: [],
      slike: []
    }
  },
  created () {
    this.fetchRodovi()
    this.fetchBiljneVrste()
    this.fetchUporabniDijelovi()
    this.fetchSlike()
  },
  methods: {
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
    fetchUporabniDijelovi () {
      this.$axios.get('http://193.198.97.14:8000/api/uporabnidijelovi/?format=json')
        .then((response) => {
          this.uporabnidijelovi = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },
    fetchSlike () {
      this.$axios.get('http://193.198.97.14:8000/api/slike/?format=json')
        .then((response) => {
          this.slike = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },
    slikeZaVrstu (id) {
      this.$axios.get('http://193.198.97.14:8000/api/slike/?format=json')
        .then((response) => {
          this.slikeZaVrstu = response.data === this.slike ? this.slike : null
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
