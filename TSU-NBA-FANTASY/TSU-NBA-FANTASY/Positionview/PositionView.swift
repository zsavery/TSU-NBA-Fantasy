//
//  Positionview.swift
//  TSU-NBA-FANTASY
//
//  Created by Jachike Uzendu on 4/23/21.
//

import Foundation
import UIKit

class PositionView: UIView {
    private static let labelBackgroundColor: UIColor = .lightGray
    
    var scoreLabel: UILabel = {
        let label = UILabel()
        label.font = UIFont.boldSystemFont(ofSize: 70)
        label.textAlignment = .center
        label.textColor = .black
        label.backgroundColor = labelBackgroundColor
        label.text = "100"
        label.sizeToFit()
        return label
    }()
    var ptsLabel = PlayerStatLabel()
    var rebLabel = PlayerStatLabel()
    var astLabel = PlayerStatLabel()
    var stlLabel = PlayerStatLabel()
    var blkLabel = PlayerStatLabel()
    var toLabel = PlayerStatLabel()
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        backgroundColor = .black
        setup()
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    func setup() {
        scoreLabel.frame = CGRect(x: 20, y: 30, width: self.bounds.width - 40, height: 100)
        addSubview(scoreLabel)
        
        let dividerView = UIView(frame: CGRect(x: 10, y: scoreLabel.frame.maxY + 30, width: self.bounds.width - 20, height: 3))
        dividerView.backgroundColor = .lightGray
        addSubview(dividerView)
        
        let topStackView = UIStackView(arrangedSubviews: [ptsLabel, rebLabel, astLabel])
        topStackView.axis = .horizontal
        topStackView.distribution = .equalCentering
        topStackView.alignment = .center
        topStackView.spacing = 35
        
        let bottomStackView = UIStackView(arrangedSubviews: [stlLabel, blkLabel, toLabel])
        bottomStackView.axis = .horizontal
        bottomStackView.distribution = .equalCentering
        bottomStackView.alignment = .center
        bottomStackView.spacing = 35
        
        let stackView = UIStackView(arrangedSubviews: [topStackView, bottomStackView])
        stackView.axis = .vertical
        stackView.distribution = .fillEqually
        stackView.alignment = .center
        stackView.frame = CGRect(x: 10, y: dividerView.frame.maxY + 30, width: self.bounds.width - 20, height: 300)
        addSubview(stackView)
    }
}

class PlayerStatLabel: UILabel {
    init(){
        super.init(frame: .zero)
        font = UIFont.boldSystemFont(ofSize: 30)
        textAlignment = .center
        textColor = .black
        backgroundColor = .lightGray
        text = "100"
        sizeToFit()
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}
