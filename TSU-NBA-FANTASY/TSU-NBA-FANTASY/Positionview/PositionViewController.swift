//
//  PositionviewController.swift
//  TSU-NBA-FANTASY
//
//  Created by Jachike Uzendu on 4/23/21.
//

import Foundation
import UIKit

class PositionViewController: UIViewController {
    var positionView: PositionView!
    let positionViewModel: PositionViewModel
    
    init(frame: CGRect) {
        self.positionViewModel = PositionViewModel()
        super.init(nibName: nil, bundle: nil)
        self.positionView = PositionView(frame: frame, delegate: self)
        self.view = self.positionView
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}

extension PositionViewController: PositionViewDelegate {
    
}
