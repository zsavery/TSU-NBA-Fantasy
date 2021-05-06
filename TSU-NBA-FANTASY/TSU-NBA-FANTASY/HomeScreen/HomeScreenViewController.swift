//
//  HomeScreenViewController.swift
//  TSU-NBA-FANTASY
//
//  Created by Jachike Uzendu on 3/15/21.
//

import Foundation
import UIKit

private let FantasyCellReusIdentifier = "FantasyCell"

protocol HomeScreenViewControllerDelegate {
    func playerSelected(player: Player)
}

class HomeScreenViewController: UIViewController {
    var homeScreenView: UITableView!
    var model: HomeScreenModel!
    private var delegate: HomeScreenViewControllerDelegate
    
    init(frame: CGRect, delegate: HomeScreenViewControllerDelegate) {
        self.delegate = delegate
        super.init(nibName: nil, bundle: nil)
        model = HomeScreenModel(delegate: self)
        self.homeScreenView = HomeScreenView(frame: frame)
        self.homeScreenView.delegate = self
        self.homeScreenView.dataSource = self
        self.view = self.homeScreenView
        self.homeScreenView.register(FantasyCell.self, forCellReuseIdentifier: FantasyCellReusIdentifier)
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
}

extension HomeScreenViewController: HomesScreenModelDelegateProtocol {
    func dataFetched() {
        DispatchQueue.main.async {
            self.homeScreenView.reloadData()
        }
    }
}

extension HomeScreenViewController: UITableViewDelegate, UITableViewDataSource {

    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return model.playerData.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        guard let fantasyCell = tableView.dequeueReusableCell(withIdentifier: FantasyCellReusIdentifier) as? FantasyCell else {
            return UITableViewCell()
        }
        let player = model.playerData[indexPath.row]
        fantasyCell.setup(name: player.name, team: player.TeamId, score: "\(player.FantasyPoints)")
        return fantasyCell
    }
    
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        let player = model.playerData[indexPath.row]
        self.delegate.playerSelected(player: player)
    }
}


class FantasyCell: UITableViewCell {
    
    private var nameLabel: UILabel = {
        let label = UILabel()
        label.font = UIFont.boldSystemFont(ofSize: 10)
        label.textAlignment = .left
        label.textColor = .gray
        return label
    }()
    
    private var teamLabel: UILabel = {
        let label = UILabel()
        label.font = UIFont.boldSystemFont(ofSize: 10)
        label.textAlignment = .left
        label.textColor = .black
        return label
    }()
    
    private var scoreLabel : UILabel = {
        let label = UILabel()
        label.font = UIFont.boldSystemFont(ofSize: 10)
        label.textAlignment = .left
        label.textColor = .gray
        return label
    }()
        
    func setup(name:String, team:String, score:String) {
        accessoryType = .disclosureIndicator
        nameLabel.text = name
        nameLabel.sizeToFit()
        teamLabel.text = team
        scoreLabel.text = score
        let stackView = UIStackView(arrangedSubviews: [nameLabel, teamLabel, scoreLabel])
        stackView.axis = .horizontal
        stackView.alignment = .center
        stackView.distribution = .equalCentering
        stackView.frame = CGRect(x: 10, y: 0, width: bounds.width - 100, height: bounds.height)
        addSubview(stackView)
    }
}
