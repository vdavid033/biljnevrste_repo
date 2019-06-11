<template>
    <q-page padding="">
        <div class="row gutter-xs">
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
        <div class="row gutter-xs">
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
                Sistemtičari:
                <div>
                    <q-input outlined v-model="sistem" label="Sistematičar" />
                </div>
            </div>
          </div>
          </div>
            <div class="col">
                Dodaj novu lat. kat.:
                <div>
                    <q-input outlined v-model="latkat" label="Lat. kategorija" />
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
                  <q-btn round color="primary" label="+" text-color="black" @click="handleClick" />
              </div>
          </div>
    <div class="q-pa-lg row">
        <div class="col">
        <q-list bordered padding class="rounded-borders">
        <q-item-label header>Izaberi botaničku porodicu</q-item-label>
        <q-item v-for="porodica in porodice" :key="porodica.id" class="q-my-sm" clickable v-ripple>
          <q-item-section>
            <q-radio v-model="radioV" :val=porodica.hrvatski_naziv_porodice />
          </q-item-section>
          <q-item-section>
            <q-item-label>
              <a :href=porodica.url>
              {{ porodica.hrvatski_naziv_porodice }}
              </a>
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
    </div>
        <div class="row gutter-xs">
          <div class="col">
              Bioaktivna tvar:
              <div>
                  <q-input outlined v-model="bioakt" label="Bioaktivna tvar" />
              </div>
          </div>
          <div class="col">
              <div class="col">
              Opis biljke:
              <div>
                  <q-input outlined v-model="opis" label="Opis" />
              </div>
          </div>
          </div>
        </div>
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
          <div class="col">
              Dodaj novi uporabni dio:
              <div>
                  <q-input outlined v-model="uporab" label="Uporabni dio" />
              </div>
          </div>
          <div class="col">
              <div>
                  <q-btn round color="primary" label="+" text-color="black" @click="handleClick" />
              </div>
          </div>
        <div class="row gutter-xs">
          <div class="col">
              Učitavanje slika:
          </div>
          <div class="col">
              <div>
                  <q-btn round color="primary" label="+" text-color="black" @click="handleClick" />
                  <q-btn round color="primary" label="+" text-color="black" @click="handleClick" />
                  <q-btn round color="primary" label="+" text-color="black" @click="handleClick" />
                  <q-btn round color="primary" label="+" text-color="black" @click="handleClick" />
                  <q-btn round color="primary" label="+" text-color="black" @click="handleClick" />
                  <q-btn round color="primary" label="+" text-color="black" @click="handleClick" />
              </div>
          </div>
        <div class="row gutter-xs">
          <div class="col">
              <div>
                  <q-btn color="white" text-color="black" label="SPREMI" />
              </div>
              <div>
              </div>
          </div>
        </div>
        </div>
    </q-page>
</template>

<script>

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
      bioaktv: '',
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
      uporabnidijelovi: []
    }
  },
  methods: {
    onItemClick () {
      console.log('Clicked on an Item')
    },
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
  }
}
</script>
