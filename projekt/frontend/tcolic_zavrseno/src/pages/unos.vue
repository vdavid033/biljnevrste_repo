<template>
    <q-page padding="">
      <div class="row" style="justify-content: center;">
      </div>
        <div class="row space-between">
            <div clas="col-6" style="width: 45%; margin-right: 5%;">
                    <q-input outlined v-model="text" label="Hrvatski naziv" :dense="dense" />
            </div>
            <div class="col-6" style="width: 45%; margin-left: 5%;">
                <q-input outlined v-model="text" label="Sinonim" :dense="dense" />
            </div>
        </div>
        <div class="row space-between" style="font-size: 1.2em;">
                Latinski naziv
        </div>
        <div class="row space-between">
            <div class="col-4" style="width: 30%; margin-right: 5%;">
                <q-input outlined v-model="text" label="Rod" :dense="dense" />
            </div>
            <div class="col-4" style="width: 30%; margin-right: 5%;">
                <q-input outlined v-model="text" label="Vrsta" :dense="dense" />
            </div>
            <div class="col-4" style="width: 30%;">
                <q-input outlined v-model="text" label="Podvrsta - SSP." :dense="dense" />
            </div>
        </div>
        <div class="row space-between">
            <div class="col-6" style="width: 45%; margin-right: 5%;">
               <q-input outlined v-model="text" label="Varijetet" :dense="dense" />
            </div>
            <div class="col-6" style="width: 45%; margin-left: 5%;">
                <q-input outlined v-model="text" label="Sistematičar" :dense="dense" />
          </div>
          </div>
        <div class="row" style="padding-bottom: 3.5%;">
            <div class="col-3" style="width: 27.5%; margin-right: 5%;">
              <div class="q-pa-md">
                <div class="q-gutter-md row">
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
                    label="Botanička porodica"
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
                <div style="padding-bottom: 5%;">
                  <q-list bordered padding class="rounded-borders" style="max-width: 300px;">
                    <q-item-label header>Odaberi botaničku porodicu:</q-item-label>
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
                <q-list bordered padding class="rounded-borders" style="max-width: 300px;">
            <q-item-label header>Odaberi uporabni dio:</q-item-label>
            <q-item  v-for="dio in uporabnidijelovi" :key="dio.id" class="q-my-sm" clickable v-ripple>
              <q-item-section>
                <q-radio v-model='radioU' :val=dio.naziv />
              </q-item-section>
              <q-item-section>
                <q-item-label title>{{ dio.naziv }}</q-item-label>
              </q-item-section>
            </q-item>
            <q-input v-model="uporab" label="Dodaj novi uporabni dio" :dense="dense" style="max-width: 308px" />
            </q-list>
              <div class="q-pa-md">
            <div class="q-px-sm">
            </div>
          </div>
            </div>
           <div class="col-8">
             <div class="row space-between" style="padding-bottom: 3.5%;">
            <div class="col-4" style="font-size: 1.2em; width: 35%; margin-right: 5%;">
                <q-input outlined v-model="text" label="Dodaj novu lat. kat." :dense="dense" />
            </div>
            <div class="col-4" style="font-size: 1.2em; width: 35%; margin-right: 5%;">
                <q-input outlined v-model="text" label="Dodaj novu hrv. kat." :dense="dense" />
            </div>
          <div class="col-4" style="font-size: 1.2em; width: 2%; margin: auto;">
              <div style="display: flex; justify-content: center;">
                  <q-btn round color="primary" label="+" text-color="black" @click="handleClick"  />
              </div>
          </div>
             </div>
             <div class="row" style="padding-bottom: 5%;">
              <q-input outlined v-model="text" style="width: 100%;" label="Bioaktivna tvar" :dense="dense" />
              </div>
              <div class="row" style="width: 100%; height: 50%; padding-bottom: 5%;">
              <q-input outlined v-model="text" style="width: 100%;height: 100%;" class="big-input" label="Opis biljke" :dense="dense" />
              </div>
              <div class="row space-between" style="font-size: 1.2em;">
              Učitavanje slika
              </div>
              <div class="row space-between" style="justify-content: space-evenly; padding-bottom: 15%;">
                        <q-btn round color="primary" label="+" text-color="black" @click="handleClick" />
                        <q-btn round color="primary" label="+" text-color="black" @click="handleClick" />
                        <q-btn round color="primary" label="+" text-color="black" @click="handleClick" />
                        <q-btn round color="primary" label="+" text-color="black" @click="handleClick" />
                        <q-btn round color="primary" label="+" text-color="black" @click="handleClick" />
                        <q-btn round color="primary" label="+" text-color="black" @click="handleClick" />
              </div>
              <div class="row space-between" style="justify-content: center;">
                    <div>
                        <q-btn color="green" text-color="black" label="SPREMI" />
                    </div>
              </div>
           </div>
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

  function newFunction() {
    return null;
  }
