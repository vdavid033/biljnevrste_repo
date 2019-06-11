<template>
    <q-page padding="">
        <div class="absolute" style="top: 0; right: 20px; transform: translateY(50%);">
          <label>Bioaktivna tvar: </label>
          <input class="form-control" type="text" v-model="search" placeholder="Search" />
        </div>
          <div class="q-pa-md">
              <label>Uporabni dio</label>
            <div class="col">
        <q-list bordered padding class="rounded-borders" style="max-width: 300px">
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
          </div>
        <table class="q-table responsive">
  <thead>
    <tr>
      <th>Botanička porodica (lat.)
        <q-item v-for="porodica in porodice" :key="porodica.ID_roda" class="q-my-sm" clickable v-ripple>
          <q-item-section>
            <q-radio v-model="radioR" :val=porodica.latisnki_naziv_porodice />
          </q-item-section>
          <q-item-section>
            <q-item-label>
              <a :href=porodica.url>
              {{ porodica.latisnki_naziv_porodice }}
              </a>
            </q-item-label>
          </q-item-section>
        </q-item>
        </th>
      <th>Rod (lat.)
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
        </th>
      <th>Porodica (hrv.)
        <q-item v-for="porodica in porodice" :key="porodica.ID_roda" class="q-my-sm" clickable v-ripple>
          <q-item-section>
            <q-radio v-model="radioR" :val=porodica.hrvatski_naziv_porodice />
          </q-item-section>
          <q-item-section>
            <q-item-label>
              <a :href=porodica.url>
              {{ porodica.hrvatski_naziv_porodice }}
              </a>
            </q-item-label>
          </q-item-section>
        </q-item>
        </th>
        <th>Vrsta
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
        </th>
    </tr>
  </thead>
</table>
<div class="row gutter-xs">
          <div class="col">
              <div>
                  <q-btn color="blue" text-color="black" class="absolute" style="right: 0; right: 800px; transform: translateY(50%);" label="PRIKAZ" />
              </div>
          </div>
        </div>
    </q-page>
</template>

<script>
export default {
  loadData () {
    this.$axios.get('http://193.198.97.14:8000/api/porodice/')
      .then((response) => {
        this.data = response.data
      })
      .catch(() => {
        this.$q.notify({
          message: 'Loading failed'
        })
      })
  },
  data () {
    return {
      myInput: '',
      text: '',
      radioU: '',
      herba: true,
      cvat: true,
      korjen: true,
      pupoljak: true,
      stabljika: true,
      hipokotil: true,
      cvijet: true,
      plod: true,
      list: true,
      petiljka: true,
      gomolj: true,
      sjeme: true,
      zadebljalikorjen: true,
      post: [],
      search: '',
      rodovi: [],
      biljnevrste: [],
      porodice: [],
      uporabnidijelovi: [],
      radioS: '',
      radioR: '',
      radioV: '',
      radioB: '',
      textLN: ''
    }
  },
  created () {
    this.fetchRodovi()
    this.fetchBiljneVrste()
    this.fetchPorodice()
    this.fetchUporabniDijelovi()
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
    fetchPorodice () {
      this.$axios.get('http://193.198.97.14:8000/api/porodice/?format=json')
        .then((response) => {
          this.porodice = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
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
    // this.kvizLink = this.links[Math.floor(Math.random() * 2)]
    setTimeout(() => {
      go()
    }, 1)
  }
}
</script>

  function newFunction() {
    return null;
  }
