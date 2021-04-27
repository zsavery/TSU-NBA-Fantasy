//
//  TopFiveView.swift
//  TSU-NBA-FANTASY
//
//  Created by Jachike Uzendu on 4/23/21.
//

import Foundation
import UIKit

protocol TopFiveViewDelegate {
    
}

class TopFiveView: UIView {
    init(frame: CGRect, delegate: TopFiveViewDelegate) {
        super.init(frame: frame)
        self.backgroundColor = UIColor.red
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}
