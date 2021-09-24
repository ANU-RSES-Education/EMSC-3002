
// Persistent variable - defaults to pretty font

if (localStorage.getItem('legibility') != 'legible') {
    localStorage.setItem('legibility', 'pretty');
}

// Action this on page load, will use persistent value

savedStyle = localStorage.getItem('legibility')
if (savedStyle == 'legible') {
    legibleFontFamily = getComputedStyle(document.documentElement).getPropertyValue('--pst-font-family-legible');
    document.documentElement.style.setProperty('--pst-font-family-base', legibleFontFamily);
    document.documentElement.style.setProperty('--pst-font-family-heading', legibleFontFamily);
}
else {
    prettyFontFamily = getComputedStyle(document.documentElement).getPropertyValue('--pst-font-family-pretty');
    document.documentElement.style.setProperty('--pst-font-family-base', prettyFontFamily);
    document.documentElement.style.setProperty('--pst-font-family-heading', prettyFontFamily);

}

// Toggle between legible and pretty fonts

function legibleFontSwitcher() {
    savedStyle = localStorage.getItem('legibility')
    if (savedStyle == 'pretty') {
        thisStyle = 'legible'
        legibleFontFamily = getComputedStyle(document.documentElement).getPropertyValue('--pst-font-family-legible');
        document.documentElement.style.setProperty('--pst-font-family-base', legibleFontFamily);
        document.documentElement.style.setProperty('--pst-font-family-heading', legibleFontFamily);
    }
    else {
        thisStyle = 'pretty'; 
        prettyFontFamily = getComputedStyle(document.documentElement).getPropertyValue('--pst-font-family-pretty');
        document.documentElement.style.setProperty('--pst-font-family-base', prettyFontFamily);
        document.documentElement.style.setProperty('--pst-font-family-heading', prettyFontFamily);
    }
    localStorage.setItem('legibility', thisStyle);
}


