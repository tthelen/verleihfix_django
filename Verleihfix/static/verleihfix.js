/**
 * Created by Tobias on 23.11.2015.
 */


$(function () {
   console.log("Off we go!");
    $('.modal-trigger').leanModal();
    $('select').material_select();
    $('.scrollspy').scrollSpy();
    //$('.pinme').pushpin({ top: $('.pinme').offset().top });
    $('.pinme').pushpin({ top: 80 });
    $(".button-collapse").sideNav();

    // German

    jQuery.extend( jQuery.fn.pickadate.defaults, {
        monthsFull: [ gettext('Januar'), gettext('Februar'), gettext('März'), gettext('April'),
                      gettext('Mai'), gettext('Juni'), gettext('Juli'), gettext('August'),
                      gettext('September'), gettext('Oktober'), gettext('November'), gettext('Dezember') ],
        monthsShort: [ gettext('Jan'), gettext('Feb'), gettext('Mär'), gettext('Apr'), gettext('Mai'), gettext('Jun'), gettext('Jul'), gettext('Aug'), gettext('Sep'), gettext('Okt'), gettext('Nov'), gettext('Dez') ],
        weekdaysFull: [ gettext('Sonntag'), gettext('Montag'), gettext('Dienstag'), gettext('Mittwoch'), gettext('Donnerstag'), gettext('Freitag'), gettext('Samstag') ],
        weekdaysShort: [ gettext('So'), gettext('Mo'), gettext('Di'), gettext('Mi'), gettext('Do'), gettext('Fr'), gettext('Sa') ],
        today: gettext('Heute'),
        clear: gettext('Löschen'),
        close: gettext('Schließen'),
        firstDay: 1,
        format: gettext('dddd, dd. mmmm yyyy'),
        formatSubmit: gettext('yyyy-mm-dd')
    });

    /*
    var from_$input = $('#input_from').pickadate(),
    from_picker = from_$input.pickadate('picker')

    var to_$input = $('#input_to').pickadate(),
    to_picker = to_$input.pickadate('picker')


    // Check if there?s a ?from? or ?to? date to start with.
    if ( from_picker.get('value') ) {
      to_picker.set('min', from_picker.get('select'))
    }
    if ( to_picker.get('value') ) {
      from_picker.set('max', to_picker.get('select'))
    }

    // When something is selected, update the ?from? and ?to? limits.
    from_picker.on('set', function(event) {
      if ( event.select ) {
        to_picker.set('min', from_picker.get('select'))
      }
      else if ( 'clear' in event ) {
        to_picker.set('min', false)
      }
    })
    to_picker.on('set', function(event) {
      if ( event.select ) {
        from_picker.set('max', to_picker.get('select'))
      }
      else if ( 'clear' in event ) {
        from_picker.set('max', false)
      }
    })
    */

    $('.datepicker').pickadate({
      selectMonths: true, // Creates a dropdown to control month
      selectYears: 5 // Creates a dropdown of 15 years to control year
    });

    function lending_calendar(year, month, lendings) {
        console.log("It's a calendar.")
        var first_of = new Date(year, month, 1).getDay();
        console.log("First is a "+first_of)
        var weekdays=[ gettext('So'), gettext('Mo'), gettext('Di'), gettext('Mi'), gettext('Do'), gettext('Fr'), gettext('Sa') ];
        var html="<h5>"+month+"/"+year+"</h5>";
        html += "<table><tr>";
        for (var i=0; i<weekdays.length; i++) {
            html += "<th style='text-align:right'>" + weekdays[i] + "</th>";
        }
        html += "</tr>";
        var day_of_month=0;
        var leap=0;
        if (((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0)) leap = 1
        var days_in_month=[31, 28+leap, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for (var i=0; i<6; i++) {
            if (day_of_month == days_in_month[month-1]+1) {
                break;
            }
            html+="<tr>";
            for (var j=0; j<7; j++) {
                console.log(day_of_month+" of "+month+":"+days_in_month[month-1])
                if (day_of_month == days_in_month[month-1]+1) {
                    break;
                }
                if (day_of_month == 0 && j == first_of) {
                    day_of_month=1;
                }
                if (day_of_month) {
                    var value = Math.random()*100
                    console.log(value)
                    var red = Math.floor(value/100 * 127)+127
                    var green = Math.floor((100 - value)/100 * 127)+127
                    cell="<td style='background-color: rgb("+red+","+green+",127); text-align: right;'>"+day_of_month+"</td>";
                    day_of_month++
                } else {
                    cell="<td></td>";
                }
                html+=cell
            }
            html+"<tr>"
        }
        html+="</table>"
        console.log(html)
        $("#lending_calendar").html(html);
    }
    lending_calendar(2015,12)
});


