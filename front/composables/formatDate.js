export function formatDate(date) {
    const js_date = new Date(date);
    // return js_date.toDateString();
    const options = {weekday: 'short', day: 'numeric', month: 'short', year:'numeric'}
    // return js_date.toLocaleDateString('pl-pl', options);
    return js_date.toLocaleDateString();
}