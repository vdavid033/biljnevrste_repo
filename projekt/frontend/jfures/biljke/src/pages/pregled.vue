<template>
    <q-page padding="">
        <div class="row">
        <div class="absolute" style="top: 0; right: 20px; transform: translateY(50%);">
          <label>Bioaktivna tvar: </label>
          <input class="form-control" type="text" v-model="search" placeholder="Search" />
        </div>
            <div class="row">
        <q-list bordered padding class="rounded-borders" style="max-width: 300px">
        <q-item-label header>Uporabni dio</q-item-label>
        <div class="q-pa-md">
            <div class="q-gutter-sm">
              <q-checkbox v-model="herba" label="herba" />
            </div>
            <div class="q-gutter-sm">
              <q-checkbox v-model="cvat" label="cvat" />
            </div>
            <div class="q-gutter-sm">
              <q-checkbox v-model="korjen" label="korjen" />
            </div>
            <div class="q-gutter-sm">
              <q-checkbox v-model="pupoljak" label="gigantski terminalni pupoljak" />
            </div>
            <div class="q-gutter-sm">
              <q-checkbox v-model="stabljika" label="stabljika" />
            </div>
            <div class="q-gutter-sm">
              <q-checkbox v-model="hipokotil" label="zadebljali hipokotil" />
            </div>
            <div class="q-gutter-sm">
              <q-checkbox v-model="cvijet" label="cvijet" />
            </div>
            <div class="q-gutter-sm">
              <q-checkbox v-model="plod" label="plod" />
            </div>
            <div class="q-gutter-sm">
              <q-checkbox v-model="list" label="list" />
            </div>
            <div class="q-gutter-sm">
              <q-checkbox v-model="petiljka" label="petiljka" />
            </div>
            <div class="q-gutter-sm">
              <q-checkbox v-model="gomolj" label="gomolj" />
            </div>
            <div class="q-gutter-sm">
              <q-checkbox v-model="sjeme" label="sjeme" />
            </div>
            <div class="q-gutter-sm">
              <q-checkbox v-model="zadebljalikorjen" label="zadebljali korjen" />
            </div>
            <div class="q-px-sm">
            </div>
          </div>
        <q-item  v-for="dio in uporabnidijelovi" :key="dio.id" class="q-my-sm" clickable v-ripple>
          <q-item-section>
            <q-item-label title>{{ dio.naziv }}</q-item-label>
          </q-item-section>
        </q-item>
        </q-list>
      </div>
      <div style="transform: translate(50%,20%);">
    <table class="q-table responsive">
      <thead>
        <tr>
          <th class="text-left">Vrsta</th>
          <th class="text-left">Rod (lat.)</th>
          <th class="text-left">Porodica (hrv.)</th>
          <th class="text-left">Botanička porodica (lat.)</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="vrsta in biljnevrste" :key="vrsta.id" class="q-my-sm" clickable v-ripple>
          <td class="text-left">
            <q-item-section><q-item-label><a :href=vrsta.url>{{ vrsta.hrvatski_naziv_vrste }}</a></q-item-label></q-item-section>
          </td>
          <td class="text-left">
            <span  v-for="rod in rodovi" :key="rod.id" class="q-my-sm" clickable v-ripple>
              <span v-if="rod.url === vrsta.ID_roda">
                <q-item-label>
                  <a :href=rod.url>
                  {{ rod.naziv_roda }}
                  </a>
                </q-item-label>
              </span>
            </span>
          </td>
          <td class="text-left">
            <span v-for="rod in rodovi" :key="rod.id" class="q-my-sm" v-ripple>
              <span v-if="rod.url === vrsta.ID_roda">
                <span v-for="porodica in porodice" :key="porodica.ID_roda" class="q-my-sm" clickable v-ripple>
                  <span v-if="rod.ID_porodice === porodica.url">
              <q-item-section>
                <q-item-label>
                  <a :href=porodica.url>
                  {{ porodica.hrvatski_naziv_porodice }}
                  </a>
                </q-item-label>
              </q-item-section>
              </span>
              </span>
              </span>
            </span>
          </td>
          <td class="text-left">
            <span v-for="rod in rodovi" :key="rod.id" class="q-my-sm" clickable v-ripple>
              <span v-if="rod.url === vrsta.ID_roda">
                <span v-for="porodica in porodice" :key="porodica.ID_roda" class="q-my-sm" clickable v-ripple>
                  <span v-if="rod.ID_porodice === porodica.url">
              <q-item-section>
                <q-item-label>
                  <a :href=porodica.url>
                  {{ porodica.latisnki_naziv_porodice }}
                  </a>
                </q-item-label>
              </q-item-section>
              </span>
              </span>
              </span>
            </span>
          </td>
        </tr>
      </tbody>
    </table>
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
      uporabnidijelovi: []
    }
  },
  created () {
    this.fetchRodovi()
    this.fetchBiljneVrste()
    this.fetchPorodice()
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
