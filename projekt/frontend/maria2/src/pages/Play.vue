<template>
    <q-page padding="">
        <div class="row gutter-xs">
            <div class="col">
                Maria test maria test
                <div>
                    <q-btn round color="primary" label="Primary" @click="handleClick" />
                    <q-input outlined v-model="myInput" label="Outlined" />
                </div>
            </div>
            <div class="col">
                Maria test maria test
            </div>
        </div>
    </q-page>
</template>

<script>
export default {
  data () {
    return {
      myInput: ''
    }
  },
  methods: {
    handleClick () {
      this.myInput = 'clicked'
    }
  }
}
</script>
