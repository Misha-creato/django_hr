    $(document).ready(function() {
        $('.custom-select').change(function() {
            $('#filter-form').submit();
        });

        $('.form-control').keypress(function(event) {
            if (event.key === 'Enter') {
                $('#filter-form').submit();
            }
        });

        $('#filter-form').submit(function(event) {
            event.preventDefault(); // Предотвращаем стандартное поведение отправки формы

            var formData = $(this).serialize();

            $.ajax({
                type: 'GET', // или 'GET', в зависимости от вашей настройки
                url: window.location.href,
                data: formData,
                success: function(data) {
                    $('#vacancies_box').html(data); // Заменяем содержимое элемента с результатами
                },
                error: function(xhr, status, error) {
                    console.error('Error:', error);
                }
            });
        });
    });
