$(document).ready(function() {
        $('#number').on("keyup", function() {
            this.value = this.value.replace(/ /g,"");
            if (!isNaN(this.value)) {
                this.value = this.value.replace(/\B(?=(\d{3})+(?!\d))/g, " ");
                $('.invalid-feedback').hide();
            } else {
                this.value = "";
                $('.invalid-feedback').show();
            }

        });
    });