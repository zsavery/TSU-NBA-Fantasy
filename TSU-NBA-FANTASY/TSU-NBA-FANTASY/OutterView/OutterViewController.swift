//
//  OutterViewController.swift
//  TSU-NBA-FANTASY
//
//  Created by Jachike Uzendu on 4/23/21.
//

import Foundation
import UIKit


struct MyResult {
    let playerId: Int
    let fisrtName: String
    let lastName: String
    let pos: String
    let teamID: String
    let points: Float
    let totReb: Float
    let assists: Float
    let steals: Float
    let blocks: Float
    let turnovers: Float
    let fantasyPoints: Float
    
    init(json: [String: Any]){
        playerId = json["playerId"] as? Int ?? 0
        fisrtName = json["fisrtName"] as? String ?? ""
        lastName = json["lastName"] as? String ?? ""
        pos = json["pos"] as? String ?? ""
        teamID = json["teamID"] as? String ?? ""
        points = json["points"] as? D ?? 0
        totReb = json["totReb"] as? Float ?? 0
        assists = json["assists"] as? Float ?? 0
        steals = json["steals"] as? Float ?? 0
        blocks = json["blocks"] as? Float ?? 0
        turnovers = json["turnovers"] as? Float ?? 0
        fantasyPoints = json["fantasyPoints"] as? Float ?? 0
    }

}


class OutterViewController: UIViewController {
    var outterView: OutterView!
    let outterViewModel: OutterViewModel!
    var homeScreenViewController: HomeScreenViewController!
    var topFiveViewController: TopFiveViewController!
    var positionViewController: PositionViewController!
    
    init(frame: CGRect) {
        self.outterViewModel = OutterViewModel()
        super.init(nibName: nil, bundle: nil)
        self.outterView = OutterView(frame: frame, delegate: self, menuOptions: self.outterViewModel.options)
        self.view = self.outterView
        setupViewControllers()
        
    let jsonUrlString = "https://tsufansite.com/info.php"
    guard let url =  URL(string: jsonUrlString) else
        {return}
    
    URLSession.shared.dataTask(with: url){(data, responce, err) in
        guard let data = data else {return}
        let dataAsString = String(data: data, encoding: .utf8)
        //print(dataAsString)
        
        do{
            let json = try JSONSerialization.jsonObject(with: data, options: [.mutableContainers, .allowFragments])
            print(json)
            
        } catch let jsonErr{
        
            print("error serializing json: ", jsonErr)
        }
        
        var newtxt: String? = dataAsString

        let wordsToRemove = ["Playerid: ", "First Name: ", "Last Name: ", "TeamID: ", "Pos: ", "Points: ", "Rebounds: ", "Assists: ", "Steals: " , "Blocks: ", "TurnOvers: ", "Fantasy "]
        for wordToRemove in wordsToRemove{
            while newtxt!.contains(wordToRemove) {
                if let range2 = newtxt!.range(of: wordToRemove) {
                    newtxt.removeSubrange(range2)
                }
            }
        }

        newtxt = newtxt.replacingOccurrences(of: " ", with: ", ")
        print("Swap spaces with commas: \n\(newtxt)")

        var txtArr = newtxt.components(separatedBy: ", ")

        //for val in txtArr{
            //print(val)
        //}
        var myNewDictArray: [[String:Any]]
        var tempDict: [String: Any]

        print("Count txtArr: \n\(txtArr.count)")

        var index = 0
        var keyNum = 12

        struct PlayerStat {
            var PlayerId: String?
            var FirstName: String?
            var LastName: String?
            var TeamId: String?
            var Pos: String?
            var Points: Double = 0
            var Rebounds: Double = 0
            var Assists : Double = 0
            var Steals: Double = 0
            var Blocks: Double = 0
            var TurnOvers: Double = 0
            var FantasyPoints: Double = 0
        }
        var stat = PlayerStat()
        var PlayerStats = [PlayerStat]()

        for value in txtArr{
            if(index > (keyNum-1)){
                index = 0
            }
            switch index {
                case 0:
                    stat.PlayerId = value
                    print("PlayerId: " + stat.PlayerId!)
                case 1:
                    stat.FirstName = value
                    print("First Name: " + stat.FirstName!)
                case 2:
                    stat.LastName = value
                    print("Last Name: " + stat.LastName!)
                case 3:
                    stat.TeamId = value
                    print("TeamId: " + stat.TeamId!)
                case 4:
                    stat.Pos = value
                    print("Position: " + stat.Pos!)
                
                case 5:
                    stat.Points = round(Double(value)!)
                    print("Points: \(stat.Points)")
                case 6:
                    stat.Rebounds = round(Double(value)!)
                    print("Rebounds: \(stat.Rebounds)")
                case 7:
                    stat.Assists = round(Double(value)!)
                    print("Assists: \(stat.Assists)")
                case 8:
                    stat.Steals = round(Double(value)!)
                    print("Steals: \(stat.Steals)")
                case 9:
                    stat.Blocks = round(Double(value)!)
                    print("Blocks: \(stat.Blocks)")
                case 10:
                    stat.TurnOvers = round(Double(value)!)
                    print("skip")
                case 11:
                    stat.FantasyPoints = round(Double(value)!)
                default:
                    print("Something went wrong!")
            }
            //print(stat)
            index+=1
            if (index == 9){
                break
            }
        }
        
        
    }.resume()
        
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    //MARK: Private
    func setupViewControllers() {
        self.homeScreenViewController = HomeScreenViewController(frame: outterView.contentView.bounds)
        self.topFiveViewController = TopFiveViewController(frame: outterView.contentView.bounds)
        self.positionViewController = PositionViewController(frame: outterView.contentView.bounds)
        guard let homeOption = self.outterViewModel.options.first else {
            return
        }
        self.menuOptionSelected(option: homeOption)
    }
}


extension OutterViewController: OutterViewDelegate {
    func menuOptionSelected(option: String) {
        self.outterView.hideMenuOptions()
        let options = outterViewModel.options
        if options.first == option {
            self.outterView.showView(view: homeScreenViewController.view, title: option)
        } else if options[1] == option {
            self.outterView.showView(view: topFiveViewController.view, title: option)
        } else  if options.last == option {
            self.outterView.showView(view: positionViewController.view, title: option)
        }
    }
    
    func menuButtonTapped() {
        self.outterView.showMenuOptions()
    }
}
