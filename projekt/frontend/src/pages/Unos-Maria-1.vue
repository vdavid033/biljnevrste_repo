<template>
    <q-page padding="">
      <div class="window-height window-width row justify-center items-center">
      <q-list bordered padding class="rounded-borders" style="width: 1300px">
        <div class="q-pa-lg row">
            <div class="col">
                Hrvatski naziv:
                <div>
                    <q-input outlined v-model="hrnaziv" label="Hrvatski naziv" />
                </div>
            </div>
            <div class="col">
                Sinonim:
                <div>
                    <q-input outlined v-model="sinonim" label="Sinonim" />
                </div>
            </div>
        </div>
        <div class="q-pa-lg row">
            <div class="col">
                Latinski naziv:
                <div>
                  <q-input outlined v-model="latnaziv" label="Latinski naziv" />
                </div>
            </div>
            <div class="col">
                Rod:
                <div>
                    <q-input outlined v-model="rod" label="Rod" />
                </div>
            </div>
            <div class="col">
                <div class="col">
                Vrsta:
                <div>
                    <q-input outlined v-model="vrsta" label="Vrsta" />
                </div>
            </div>
            </div>
            <div class="col">
                Podvrsta-ssp.:
                <div>
                    <q-input outlined v-model="podvrsta" label="Podvrsta" />
                </div>
            </div>
            <div class="col">
                Varijetet:
                <div>
                    <q-input outlined v-model="varijetet" label="Varijetet" />
                </div>
            </div>
            <div class="col">
                <div class="col">
                Sistemtičar:
                <div>
                    <q-input outlined v-model="sistem" label="Sistematičar" />
                </div>
            </div>
          </div>
          </div>
    <div class="q-pa-lg row">
        <div class="col">
          Izaberi botaničku porodicu:
        <q-list bordered padding class="rounded-borders" style="max-width: 350px">
        <q-item v-for="porodica in porodice" :key="porodica.id" class="q-my-sm" clickable v-ripple>
          <q-item-section>
            <q-radio v-model="radioV" :val=porodica.hrvatski_naziv_porodice />
          </q-item-section>
          <q-item-section>
            <q-item-label>
              {{ porodica.hrvatski_naziv_porodice }}
            </q-item-label>
          </q-item-section>
          <q-item-section>
            <q-item-label>
              (lat. {{ porodica.latisnki_naziv_porodice }})
            </q-item-label>
          </q-item-section>
        </q-item>
        </q-list>
      </div>
      <!-- end vd -->
                  <div class="col">
                Dodaj novu lat. kat.:
                <div>
                    <q-input outlined v-model="latkat" label="Lat. kategorija"/>
                </div>
            </div>
            <div class="col">
                <div class="col">
                Dodaj novu hrv. kat.:
                <div>
                    <q-input outlined v-model="hrvkat" label="Hr. kategorija" />
                </div>
            </div>
            </div>
          <div class="col">
              <div>
                  <q-btn round color="primary" label="+" text-color="black" @click="dodajKategoriju" />
              </div>
          </div>
    </div>
        <div class="q-pa-lg row">
          <div class="col">
            <q-list bordered padding class="rounded-borders" style="max-width: 300px">
            <q-item-label header>Odaberi uporabni dio:</q-item-label>
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
              Dodaj novi uporabni dio:
              <div>
                  <q-input outlined v-model="uporab" label="Uporabni dio" style="max-width: 308px" />
              </div>
              <q-list bordered padding class="rounded-borders" style="max-width: 308px">
              <q-item-label header>Opis biljke:</q-item-label>
              <div class="q-pa-md" style="max-width: 300px">
                <q-input
                  v-model="text"
                  filled
                  type="textarea"
                />
              </div>
              </q-list>
          </div>
          <div class="col">
              <div>
                  <q-btn round color="primary" label="+" text-color="black" @click="dodajUporabnidio"/>
              </div>
          </div>
          </div>
        <div class="q-pa-lg row justify-center">
    <div class="q-gutter-md">
      Učitavanje slika:
      <q-btn round color="primary" label="+" text-color="black" :key="`md-${n}`" @click="$router.push('/unosslike')"/>
            <q-btn round color="primary" label="+" text-color="black" :key="`md-${n}`" @click="$router.push('/unosslike')"/>
                  <q-btn round color="primary" label="+" text-color="black" :key="`md-${n}`" @click="$router.push('/unosslike')"/>
                        <q-btn round color="primary" label="+" text-color="black" :key="`md-${n}`" @click="$router.push('/unosslike')"/>
                              <q-btn round color="primary" label="+" text-color="black" :key="`md-${n}`" @click="$router.push('/unosslike')"/>
                                    <q-btn round color="primary" label="+" text-color="black" :key="`md-${n}`" @click="$router.push('/unosslike')"/>
                                    <q-btn color="primary" text-color="black" label="SPREMI" @click="spremi"/>
    </div>
            </div>
  <div class="q-pa-md">
    <div class="q-gutter-md row">
            Botanička porodica:
      <q-select
        filled
        v-model="model"
        use-input
        hide-selected
        fill-input
        input-debounce="0"
        :options="options"
        @filter="filterFn"
        hint="Odaberi"
        style="width: 250px; padding-bottom: 32px"
      >
        <template v-slot:no-option>
          <q-item>
            <q-item-section class="text-grey">
              No results
            </q-item-section>
          </q-item>
        </template>
      </q-select>
    </div>
  </div>
  </q-list>
  </div>
    </q-page>
</template>

<script>

const stringOptions = [
  'porodica1', 'porodica2', 'porodica3', 'porodica4', 'porodica5'
]

export default {
  data () {
    return {
      hrnaziv: '',
      sinonim: '',
      latnaziv: '',
      rod: '',
      vrsta: '',
      podvrsta: '',
      varijetet: '',
      sistematicar: '',
      latkat: '',
      hrvkat: '',
      uporab: '',
      opis: '',
      text: '',
      sistem: '',
      hrvatskiNaziv: '',
      radioS: '',
      radioR: '',
      radioV: '',
      radioU: '',
      radioB: '',
      textLN: '',
      porodice: [],
      uporabnidijelovi: [],
      model: null,
      options: stringOptions
    }
  },
  methods: {
    fetchPorodice () {
      this.$axios.get('http://193.198.97.14:8000/api/porodice/?format=json')
        .then((response) => {
          this.porodice = response.data
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
  created () {
    this.fetchPorodice()
    this.fetchUporabniDijelovi()
  },
  filterFn (val, update, abort) {
    update(() => {
      const needle = val.toLowerCase()
      this.options = stringOptions.filter(v => v.toLowerCase().indexOf(needle) > -1)
    })
  },
  dodajUporabnidio () {
    this.$alert(this.uporab)
  },
  dodajKategoriju () {
  },
  spremi () {
  }
}
</script>
