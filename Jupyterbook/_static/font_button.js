
// Persistent variable - defaults to pretty font

if (localStorage.getItem('legibility') != 'legible') {
    localStorage.setItem('legibility', 'pretty');
}

// Action this on page load, will use persistent value

savedStyle = localStorage.getItem('legibility')
if (savedStyle == 'legible') {
    legibleFontFamily = getComputedStyle(document.documentElement).getPropertyValue('--pst-font-family-legible');
    legibleFontFamilyH = getComputedStyle(document.documentElement).getPropertyValue('--pst-font-family-legible-headers');
    document.documentElement.style.setProperty('--pst-font-family-base', legibleFontFamily);
    document.documentElement.style.setProperty('--pst-font-family-heading', legibleFontFamilyH);
}
else {
    prettyFontFamily = getComputedStyle(document.documentElement).getPropertyValue('--pst-font-family-pretty');
    prettyFontFamilyH = getComputedStyle(document.documentElement).getPropertyValue('--pst-font-family-pretty-headers');
    document.documentElement.style.setProperty('--pst-font-family-base', prettyFontFamily);
    document.documentElement.style.setProperty('--pst-font-family-heading', prettyFontFamilyH);

}

// Toggle between legible and pretty fonts

function legibleFontSwitcher() {
    savedStyle = localStorage.getItem('legibility')
    if (savedStyle == 'pretty') {
        thisStyle = 'legible'
        legibleFontFamily = getComputedStyle(document.documentElement).getPropertyValue('--pst-font-family-legible');
        legibleFontFamilyH = getComputedStyle(document.documentElement).getPropertyValue('--pst-font-family-legible-headers');
        document.documentElement.style.setProperty('--pst-font-family-base', legibleFontFamily);
        document.documentElement.style.setProperty('--pst-font-family-heading', legibleFontFamilyH);
    }
    else {
        thisStyle = 'pretty'; 
        prettyFontFamily = getComputedStyle(document.documentElement).getPropertyValue('--pst-font-family-pretty');
        prettyFontFamilyH = getComputedStyle(document.documentElement).getPropertyValue('--pst-font-family-pretty-headers');
        document.documentElement.style.setProperty('--pst-font-family-base', prettyFontFamily);
        document.documentElement.style.setProperty('--pst-font-family-heading', prettyFontFamilyH);
    }
    localStorage.setItem('legibility', thisStyle);
}


