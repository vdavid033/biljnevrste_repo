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
    <div class="q-pa-lg row">
      <!--vd -->
      <div class="col">
        <q-list bordered padding class="rounded-borders" style="max-width: 300px">
        <q-item-label header>Izaberi botaničku porodicu</q-item-label>
        <q-item v-for="porodica in porodice" :key="porodica.id" class="q-my-sm" clickable v-ripple>
          <q-item-section>
            <q-radio v-model="radioR" :val=porodica.naziv_roda />
          </q-item-section>
          <q-item-section>
            <q-item-label>
              <a :href=porodica.url>
              {{ porodica.hrvatski_naziv_porodice }}
              </a>
            </q-item-label>
          </q-item-section>
        </q-item>
        </q-list>
      </div>
      <!-- end vd -->
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
        <div class="row gutter-xs">
          <div class="col">
              Uporabni dio:
          </div>
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
                  <q-input outlined v-model="opis" label="Oopis" />
              </div>
          </div>
          </div>
        </div>
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
          <div class="q-pa-lg text-weight-bold q-display-2">
            {{this.rod.naziv_roda}}
          </div>
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
      loading: true,
      sistem: '',
      radioR: '',
      porodice: []
    }
  },
  methods: {
    onItemClick () {
      console.log('Clicked on an Item')
    },
    fetchBiljneVrste () {
      this.$axios.get('http://193.198.97.14:8000/api/porodice/?format=json')
        .then((response) => {
          this.porodice = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  created () {
    this.loadData()
  }
}
</script>
