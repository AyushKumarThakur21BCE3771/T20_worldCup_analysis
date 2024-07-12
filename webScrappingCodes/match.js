/* -------------- STAGE 1 ------------ */

//Interaction Code

navigate('https://www.espncricinfo.com/records/tournament/team-match-results/icc-men-s-t20-world-cup-2024-15946');
collect(parse());



//Parser Code
let matchSummary = []

const allRows = $('table.engineTable > tbody > tr.data1');

 allRows.each((index, element) => {
 		const tds = $(element).find('td');   
		matchSummary.push({
              'team1':  $(tds[0]).text(),
              'team2':  $(tds[1]).text(),
              'winner':  $(tds[2]).text(),
              'margin':  $(tds[3]).text(),
              'ground': $(tds[4]).text(),
              'matchDate': $(tds[5]).text(),
              'scorecard':   $(tds[6]).text() 
		})   
 })

return {
  "matchSummary": matchSummary
};