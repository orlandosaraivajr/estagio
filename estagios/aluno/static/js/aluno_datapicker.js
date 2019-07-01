$(function () {
    // Sobre Mim
    $("#id_sobre_voce").focus();

    $("#id_data_nascimento").datetimepicker({
        sideBySide: true,
        format: 'DD/MM/YYYY'
    });

    // Faculdade

    $("#id_data_inicio").datetimepicker({
        sideBySide: true,
        format: 'DD/MM/YYYY'
    });
    $("#id_data_fim").datetimepicker({
        sideBySide: true,
        format: 'DD/MM/YYYY'
    });
});